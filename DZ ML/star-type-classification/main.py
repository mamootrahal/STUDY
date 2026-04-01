import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score



# ==============================
# 1. Чтение данных
# ==============================
# Если у тебя файлы называются иначе (например train_star.csv),
# просто поменяй имена здесь.
train = pd.read_csv("train_star.csv")
test = pd.read_csv("test_star.csv")


# ==============================
# 2. Функция для создания простых признаков
# ==============================
def add_features(df):
    df = df.copy()

    # Относительная ошибка параллакса:
    # чем она больше, тем менее надёжен параллакс
    df["plx_rel_error"] = df["e_Plx"] / (df["Plx"].abs() + 1e-6)

    # Оценка температуры по индексу цвета B-V
    # Это известная приближённая формула
    bv = df["B-V"]
    df["temp_est"] = 4600 * (
        1 / (0.92 * bv + 1.7) + 1 / (0.92 * bv + 0.62)
    )

    # Выделяем первую букву спектрального класса: O, B, A, F, G, K, M
    df["SpecLetter"] = (
        df["SpType"]
        .str.extract(r"([OBAFGKM])", expand=False)
        .fillna("Unknown")
    )

    # Выделяем класс светимости, если он встречается в строке
    # Например: I, II, III, IV, V
    df["LumClass"] = (
        df["SpType"]
        .str.extract(r"(Ia\+|Ia0|Ia|Iab|Ib|II|III|IV|V|VI|VII)", expand=False)
        .fillna("Unknown")
    )

    return df


train = add_features(train)
test = add_features(test)


# ==============================
# 3. Целевая переменная
# ==============================
# В train целевая переменная хранится как текст:
# Dwarf / Giant
# По условию сабмита нужны числа:
# Dwarf -> 0
# Giant -> 1
target_map = {
    "Dwarf": 0,
    "Giant": 1
}

train["TargetClass"] = train["TargetClass"].map(target_map)


# ==============================
# 4. Делим на признаки и ответ
# ==============================
X = train.drop(columns=["TargetClass"])
y = train["TargetClass"]


# ==============================
# 5. Какие признаки категориальные, какие числовые
# ==============================
categorical_features = ["SpType", "SpecLetter", "LumClass"]
numeric_features = [col for col in X.columns if col not in categorical_features]


# ==============================
# 6. Предобработка
# ==============================
# Строковые признаки превращаем в набор бинарных столбцов
# Числовые просто передаём как есть
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("num", "passthrough", numeric_features)
    ]
)


# ==============================
# 7. Модель
# ==============================
# RandomForest — довольно простой и понятный метод
model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced"
)


# ==============================
# 8. Общий pipeline
# ==============================
pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", model)
])


# ==============================
# 9. Проверка качества на валидации
# ==============================
X_train, X_valid, y_train, y_valid = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

pipeline.fit(X_train, y_train)

valid_pred = pipeline.predict(X_valid)

f1 = f1_score(y_valid, valid_pred)
print("F1-score на валидации:", f1)


# ==============================
# 10. Обучаемся на всём train
# ==============================
pipeline.fit(X, y)


# ==============================
# 11. Предсказание для test
# ==============================
test_pred = pipeline.predict(test)


# ==============================
# 12. Формируем submission
# ==============================
# В test.csv столбца index может не быть,
# поэтому делаем его сами: 0, 1, 2, ...
submission = pd.DataFrame({
    "index": np.arange(len(test)),
    "TargetClass": test_pred.astype(int)
})

submission.to_csv("submission.csv", index=False)

print("Файл submission.csv сохранён.")
print(submission.head())
import pandas as pd
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import KFold, cross_val_score

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

target_col = "Health index"
feature_cols = [col for col in train.columns if col != target_col and col in test.columns]

X = train[feature_cols]
y = train[target_col]
X_test = test[feature_cols]

model = ExtraTreesRegressor(
    n_estimators=500,
    random_state=42,
    n_jobs=-1
)

cv = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(
    model,
    X,
    y,
    cv=cv,
    scoring="neg_mean_squared_error",
    n_jobs=-1
)

mse_scores = -cv_scores
print("CV MSE по фолдам:", mse_scores)
print("Средний CV MSE:", mse_scores.mean())

model.fit(X, y)
preds = model.predict(X_test)

submission = pd.DataFrame({
    "index": test["index"],
    "Health index": preds
})

submission.to_csv("submission.csv", index=False)
print("Файл submission.csv сохранён.")
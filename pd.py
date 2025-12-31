import pandas as pd
import numpy as np
import sys
from io import StringIO

data = sys.stdin.read().strip()
if data:
    df = pd.read_csv(StringIO(data))
else:
    df = pd.read_csv("input.csv")  # stdin — это “файл”, pandas умеет
# df =  pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9], "d": [10, 11, 12], "e": [13, 14, 15]})  # читать из него напрямую
# print(df)
# print("Первые строки", df.head(5),       # первые строки
# "последние строки", df.tail(5),       # последние строки
# "строки, столбцы", df.shape,         # (строки, столбцы)
# "имена столбцов", df.columns,       # имена столбцов
# "типы", df.dtypes,        # типы
# "сводка", df.info(), # сводка
# "статистика по числам", df.describe())   # статистика по числам
#print(df.columns.tolist())
#print([repr(c) for c in df.columns])

counts = df["Имя"].value_counts()
print("counts:", counts)
mx = counts.max()
print("mx:", mx)
top = counts[counts == mx].sort_index()   # алфавитный порядок
print("top:", top)

for name, c in top.items():
    print(name, c)

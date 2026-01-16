import pandas as pd
import numpy as np
import sys
from io import StringIO
import math



df = pd.read_csv("input.csv")  # stdin — это “файл”, pandas умеет
#print(df)
#print(df["Tectonic regime"])
s = (
    df["Tectonic regime"]
    .astype(str)
    .str.split(r"\s*/\s*")
    .explode()
    .dropna()
    .str.strip()
)
#print(s)



unique_regimes = sorted(s.unique())

print(len(unique_regimes))
for x in unique_regimes:
    print(x)
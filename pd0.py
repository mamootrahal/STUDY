import pandas as pd
import numpy as np
import sys
from io import StringIO
import math

#ppi  = hxl / diag
df = pd.read_csv("input.csv")  # stdin — это “файл”, pandas умеет
df["ScreenResolution"] = df["ScreenResolution"].str.split().str[-1].str.split("x")
#print(df.loc[0, "ScreenResolution"][1])
for i in range(len(df)):
    l = int(df.loc[i, "ScreenResolution"][0])
    h = int(df.loc[i, "ScreenResolution"][1])
    df.loc[i, "ppi"] = math.sqrt(h * h + l* l) / df.loc[i, "Inches"]

print(round(df["ppi"].mean(), 2))


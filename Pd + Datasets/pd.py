import pandas as pd

df = pd.read_csv(r"Pd + Datasets\Price_euros_train.csv")
dfID = df["laptop_ID"]
dfMemory = df["Memory"]

def to_gb(x):
    x = str(x).upper().strip()
    if x.endswith("TB"):
        return int(float(x[:-2]) * 1024)
    if x.endswith("GB"):
        return int(float(x[:-2]))
    return int(float(x))

dfDD = pd.DataFrame({
    "laptop_ID": dfID,
    "SSD": 0,
    "HDD": 0,
    "Hybrid": 0,
    "Flash Storage": 0
}).astype({"SSD": "int64", "HDD": "int64", "Hybrid": "int64", "Flash Storage": "int64"})

for i in range(len(df)):
    parts = str(dfMemory.iloc[i]).split("+")
    print(parts)

    for part in parts:
        s = part.strip().split()
        if len(s) < 2:
            continue

        size = to_gb(s[0])

        if s[1] == "SSD":
            dfDD.loc[i, "SSD"] = size
        elif s[1] == "HDD":
            dfDD.loc[i, "HDD"] = size
        elif s[1] == "Hybrid":
            dfDD.loc[i, "Hybrid"] = size
        elif s[1] == "Flash":                  
            dfDD.loc[i, "Flash Storage"] = size

#dfDD = dfDD.sort_values("laptop_ID", ascending = True)
# dfDD.to_csv(r"Pd + Datasets\dfDD.csv", index=False, encoding="utf-8")

# print(dfDD.to_csv(index=False), end="")

dfDD.to_csv(r"Pd + Datasets\output.csv", index=False, encoding="utf-8")
csv_text1 = dfDD.to_csv(index=False)  # по умолчанию с заголовками


dfAns = pd.read_csv(r"Pd + Datasets\ans.csv")
csv_text2 = dfAns.to_csv(index = False)
[]



print(csv_text2)
for i in range(len(csv_text1)):
    if csv_text1[i] != csv_text2[i]:
        print("XYITA", i)
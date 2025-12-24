import numpy as np
import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter("ignore")
np.seterr(all='ignore')
# ХЗ!!
def cosd(A, i):
    x = A[i]
    y = A[i+1]
    norm = np.linalg.norm(x) * np.linalg.norm(y)
    return x @ y / (norm)

data = []
while True:
    try:
        line = input()
    except EOFError:
        break
    line = line.strip()
    if line:
        data.append(list(map(float, line.split())))

if len(data) < 2:
    print("No solution")

A = np.array(data, dtype=float)


ans = float(0)
Ans = np.empty((A.shape[0], A.shape[0]), dtype=float)

try:
    for i in range(A.shape[0] - 1):
        for j in range(A.shape[0] - 1):
            Ans[i, j] = cosd(A, i)
    ans = np.min(Ans)
except Exception:
    ans = float('nan')

if ans >= -1.0 and ans <= 1.0 and len(data) >= 2:
    print(f"{ans:.2f}")
elif np.isnan(ans):
    print("No solution")

    
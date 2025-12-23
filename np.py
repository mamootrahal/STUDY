import numpy as np

def cosd(x, y):
    return x @ y / (np.linalg.norm(x) * np.linalg.norm(y))

data = []
while True:
    try:
        line = input()
    except EOFError:
        break
    line = line.strip()
    if line:
        data.append(list(map(float, line.split())))

A = np.array(data, dtype=float)

ans = float(0)
Ans = np.empty(A.shape[0], dtype=float)

for i in range(A.shape[0] - 1):
    Ans[i] = cosd(A[i], A[i+1])

ans = np.max(Ans)

if ans >= 0.0 and ans <= 1.0:
    print(f"{ans:.2f}")
else:
    print("No solution")
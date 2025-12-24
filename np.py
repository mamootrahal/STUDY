import numpy as np
# import warnings
# warnings.filterwarnings("ignore")
# warnings.simplefilter("ignore")
# np.seterr(all='ignore')

def InputMatrix(typeX):
    data = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        line = line.strip()
        if line:
            data.append(list(map(typeX, line.split())))
    return np.array(data, dtype=typeX)



k = int(input())
A = InputMatrix(int)
n, m = A.shape

out_rows = int(np.ceil(n / k))
out_cols = int(np.ceil(m / k))
out = np.empty((out_rows, out_cols), dtype=int)

r = 0
for i in range(0, n, k):
    c = 0
    for j in range(0, m, k):
        out[r, c] = A[i:i+k, j:j+k].sum()
        c += 1
    r += 1

for row in out:
    print(*row)
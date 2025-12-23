import numpy as np

data = []
while True:
    try:
        line = input()
    except EOFError:
        break
    line = line.strip()
    if line:
        data.append(list(map(int, line.split())))

A = np.array(data, dtype=int)
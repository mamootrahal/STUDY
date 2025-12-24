import numpy as np
import warnings


def IgnoreNanInfs():
    warnings.filterwarnings("ignore")
    warnings.simplefilter("ignore")
    np.seterr(all='ignore')

def InputMatrixFloat():
    data = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        line = line.strip()
        if line:
            data.append(list(map(float, line.split())))
    return np.array(data, dtype=float)

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
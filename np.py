import numpy as np
# import warnings
# warnings.filterwarnings("ignore")
# warnings.simplefilter("ignore")
# np.seterr(all='ignore')

def get_nearest (l):
    t = l.copy()
    l= np.abs(l)
    i = np.where(l == np.min(l))[0][0]
    min_val = t[i]
    return min_val

A = np.array(list(map(int, input().split())))
print(get_nearest(A))
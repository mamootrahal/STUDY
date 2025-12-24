import pandas as pd

def mean_xy_with_error(x, y):

    s = (x + y)/2*(1+error)  

    error += 0.01

    return s

error = 0.05

print(mean_xy_with_error(1,2))



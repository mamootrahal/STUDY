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

nums = list(map(int, input().split()))

cur = best = nums[0]
for x in nums[1:]:
    cur = max(x, cur + x)
    best = max(best, cur)

print(best)
print(nums[1:])
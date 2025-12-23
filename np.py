import numpy as np

# a = np.array([[1, 2],
#               [3, 4]])   # shape (2, 2)

# b = np.array([[5, 6],
#               [7, 8]])   # shape (2, 2)


# print(np.concatenate([a, b], axis=0), type(np.concatenate([a, b], axis=0)))
# # shape станет (4, 2)

# print(np.concatenate([a, b], axis=1))
# # shape станет (2, 4)
# print('_' * 20)

# a = np.array([[1, 2, 3], 
#               [4, 5, 6]])
# print(a.shape)

# 8*5
# 0 0 1 0 0 
# 0 1 0 0 0 
# 0 1 1 1 1 
# 0 1 0 0 0 
# 1 1 0 1 0 
# 1 1 1 0 1 
# 1 1 1 0 0 
# 1 0 0 1 1 

c = 0

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

n = A.shape[1]

for i in range(n):
    if all(A[:, i] == 0):
        c += 1

print(c)
n_v = int(input()) # кол-во весов
weights = list(map(int, input().split(' '))) # веса
b = int(input()) # смещение
x = list(map(int, input().split(' '))) # входные данные

if len(weights) != n_v or len(x) != n_v:
    print("No solution")
else:
    s = sum([weights[i] * x[i] for i in range(n_v)]) + b
    print(max(0, s))
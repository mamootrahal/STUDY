k = list(map(int, input().split(' ')))

# ax² + bx + c = d
# a b c d
# 0 1 2 3
k = [k[0], k[1], k[2] - k[3]]

D = k[1] * k[1] - 4 * k[0] * k[2]

if k[0] == 0:
    if k[1] == 0:
        if k[2] == 0:
            print(-1)  # бесконечно много решений
        else:
            print(0)   # нет решений
    else:
        print(1)       # линейное, одно решение

else:
    if D < 0:
        print("0")
    elif D == 0:
        print("1")
    elif D > 0:
        print("2")
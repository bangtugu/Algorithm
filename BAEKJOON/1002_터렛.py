# 3
# 0 0 13 40 0 37
# 0 0 3 0 7 4
# 1 1 1 1 1 5

def calc(x1, y1, z1, x2, y2, z2):

    d = abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2

    if d == 0 and z1 == z2:
        return -1

    if d == (z1 + z2) ** 2 or d == (z1 - z2) ** 2:
        return 1
    elif (z1 - z2) ** 2 < d < (z1 + z2) ** 2:
        return 2
    else:
        return 0


T = int(input())

answer = []

for test_case in range(T):
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    print(calc(x1, y1, z1, x2, y2, z2))
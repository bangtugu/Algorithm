import sys
sys.stdin = open('2636_input.txt', 'r')
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def air_check():

    v = [[0] * mx for _ in range(my)]

    v[0][0] = 1
    Q = deque()
    Q.append((0, 0))
    cheese = 0

    while Q:
        y, x = Q.popleft()

        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < my and 0 <= xx < mx and not v[yy][xx]:
                if table[yy][xx] == 0:
                    v[yy][xx] = 1
                    Q.append((yy, xx))
                if table[yy][xx] == 1:
                    v[yy][xx] = 1
                    cheese += 1
                    table[yy][xx] = 0

    return cheese


my, mx = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(my)]

cheese_lst = []
t = -1
while True:
    t += 1
    check = air_check()
    if check == 0:
        break
    cheese_lst.append(check)


print(t)
print(cheese_lst[-1])
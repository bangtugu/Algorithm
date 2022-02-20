import sys
sys.stdin = open('2178_input.txt', 'r')
from collections import deque

T = int(input())

for test_case in range(1, T+1):
    my, mx = map(int, input().split())
    table = [[0]*mx for _ in range(my)]

    for i in range(my):
        now = input()
        for j in range(mx):
            if int(now[j]):
                table[i][j] = my * mx
            else:
                table[i][j] = 0

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    Q = deque()
    Q.append((0, 0))
    table[0][0] = 1

    while Q:
        y, x = Q.popleft()
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < my and 0 <= xx < mx and table[yy][xx]:
                if table[yy][xx] > table[y][x] + 1:
                    table[yy][xx] = table[y][x] + 1
                    Q.append((yy, xx))


    print('#{} {}'.format(test_case, table[my-1][mx-1]))


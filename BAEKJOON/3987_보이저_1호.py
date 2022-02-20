import sys
sys.stdin = open('3987_input.txt', 'r')
from collections import deque


di = ['U', 'R', 'D', 'L']
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    space = [input() for _ in range(N)]
    PR, PC = map(int, input().split())
    PR -= 1
    PC -= 1

    max_signal = 0
    max_d = ''
    for i in range(4):
        # print(di[i])
        signal = 0
        Q = deque()
        Q.append([PR, PC, i])
        while Q:
            y, x, d = Q.popleft()
            yy = y + dy[d]
            xx = x + dx[d]
            signal += 1

            if 0 > yy or yy == N or 0 > xx or xx == M:
                if signal > max_signal:
                    max_signal = signal
                    max_d = di[i]
                break

            if space[yy][xx] == '/':
                if d % 2:
                    dd = d - 1
                else:
                    dd = d + 1
            elif space[yy][xx] == '\\':
                if d % 2:
                    dd = (d + 1) % 4
                else:
                    dd = 3 - d
            elif space[yy][xx] == 'C':
                break
            else:
                dd = d

            # print(yy, xx, dd, space[yy][xx])

            if [yy, xx, dd] == [PR, PC, i]:
                max_signal = 'Voyager'
                max_d = di[i]
                break
            else:
                Q.append([yy, xx, dd])

        if max_signal == 'Voyager':
            break

    print(max_d)
    print(max_signal)
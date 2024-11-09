import sys
input = sys.stdin.readline
from collections import deque

W, H = map(int, input().split())
table = [input() for _ in range(H)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
check = [[[-1]*2 for _ in range(W)] for _ in range(H)]

answer = -1
Q = deque()
for i in range(H):
    for j in range(W):
        if table[i][j] == 'C':
            for d in range(4):
                ny = i + dy[d]
                nx = j + dx[d]

                while 0 <= ny < H and 0 <= nx < W and table[ny][nx] != '*':
                    if table[ny][nx] == 'C':
                        answer = 0
                        break
                    elif table[ny][nx] == '.':
                        check[ny][nx][d%2] = 0
                        Q.append([ny, nx, d%2])
                    else:
                        break

                    ny += dy[d]
                    nx += dx[d]
            
            check[i][j] = [0, 0]
        if Q: break
    if Q: break

while Q and answer == -1:
    y, x, nowd = Q.popleft()

    for d in [(nowd+1)%4, (nowd-1)%4]:
        ny = y + dy[d]
        nx = x + dx[d]
        while 0 <= ny < H and 0 <= nx < W and check[ny][nx][d%2] == -1:
            if table[ny][nx] == 'C':
                answer = check[y][x][nowd] + 1
                break
            elif table[ny][nx] == '.':
                check[ny][nx][d%2] = check[y][x][nowd] + 1
                Q.append([ny, nx, d%2])
            else:
                break

            ny += dy[d]
            nx += dx[d]

print(answer)


'''

7 8
.......
......C
......*
*****.*
....*..
....*..
.C..*..
.......

'''
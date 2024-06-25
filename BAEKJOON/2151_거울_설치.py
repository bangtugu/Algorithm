import sys
input = sys.stdin.readline

N = int(input())
room = [input() for _ in range(N)]
check = [[[N*N, N*N, N*N, N*N] for _ in range(N)] for _ in range(N)]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
start = []
ey, ex = 0, 0

for i in range(N):
    for j in range(N):
        if room[i][j] == '#':
            if not start:
                for d in range(4):
                    ni, nj = i+dy[d], j+dx[d]
                    if ni < 0 or nj < 0 or ni >= N or nj >= N: continue
                    if room[ni][nj] == '*': continue
                    start.append([i, j, d])
                    check[i][j][d] = 0
            else:
                ey, ex = i, j

from collections import deque
Q = deque()
for y, x, d in start:
    Q.append([y, x, d])

while Q:
    y, x, d = Q.popleft()
    ny, nx = y+dy[d], x+dx[d]
    while 0 <= ny < N and 0 <= nx < N and room[ny][nx] != '*':
        if check[ny][nx][d] <= check[y][x][d]:
            break

        check[ny][nx][d] = check[y][x][d]
        if room[ny][nx] == '!':
            for nd in range(4):
                if nd//2 == d//2: continue
                if check[ny][nx][nd] <= check[y][x][d] + 1: continue
                check[ny][nx][nd] = check[y][x][d] + 1
                Q.append([ny, nx, nd])

        ny += dy[d]
        nx += dx[d]
        
    if min(check[ey][ex]) != N*N:
        break

print(min(check[ey][ex]))

'''

5
***#*
*.!.*
*!.!*
*.!.*
*#***

'''
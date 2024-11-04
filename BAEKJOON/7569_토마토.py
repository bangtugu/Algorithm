import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())
tomatos = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
Q = deque()
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

fresh_tomato = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if tomatos[h][i][j] == 1:
                Q.append([h, i, j])
            if tomatos[h][i][j] == 0:
                fresh_tomato += 1

answer = -1
while Q:
    h, y, x = Q.popleft()
    answer = max(answer, tomatos[h][y][x]-1)

    for d in range(6):
        nh = h + dh[d]
        ny = y + dy[d]
        nx = x + dx[d]

        if nh < 0 or ny < 0 or nx < 0 or nh >= H or ny >= N or nx >= M or tomatos[nh][ny][nx] != 0: continue
        tomatos[nh][ny][nx] = tomatos[h][y][x] + 1
        fresh_tomato -= 1
        Q.append([nh, ny, nx])

print(-1 if fresh_tomato else answer)
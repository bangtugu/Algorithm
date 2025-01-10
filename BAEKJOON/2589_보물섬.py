import sys
input = sys.stdin.readline

N, M = map(int, input().split())
island = [input() for _ in range(N)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
from collections import deque


def exp(sy, sx):
    cost = [[0]*M for _ in range(N)]
    cost[sy][sx] = 1
    Q = deque()
    Q.append([sy, sx])

    while Q:
        y, x = Q.popleft()

        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]

            if ny < 0 or nx < 0 or ny >= N or nx >= M or island[ny][nx] == 'W' or cost[ny][nx]: continue
            cost[ny][nx] = cost[y][x] + 1
            Q.append([ny, nx])
    
    return cost[y][x]-1


answer = 0
for i in range(N):
    for j in range(M):
        if island[i][j] == 'W': continue
        answer = max(answer, exp(i, j))

print(answer)
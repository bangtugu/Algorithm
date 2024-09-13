import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mapp = []
start = [-1, -1]

for i in range(N):
    line = list(map(int, input().split()))
    mapp.append(line)
    if sum(start) >= 0: continue
    for j in range(M):
        if line[j] == 2:
            start = [i, j]
            break

from collections import deque
answer = [[-1]*M for _ in range(N)]
answer[start[0]][start[1]] = 0
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
Q = deque([start])

while Q:
    y, x = Q.popleft()

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if ny < 0 or nx < 0 or ny >= N or nx >= M or mapp[ny][nx] == 0 or answer[ny][nx] != -1: continue
        Q.append([ny, nx])
        answer[ny][nx] = answer[y][x] + 1
        

for i in range(N):
    for j in range(M):
        if mapp[i][j] == 0:
            answer[i][j] = 0

for line in answer:
    print(*line)
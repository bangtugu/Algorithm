import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
before = [list(map(int, input().split())) for _ in range(N)]
after = [list(map(int, input().split())) for _ in range(N)]
check = [[0]*M for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def bfs(i, j, n):
    Q = deque()
    Q.append([i, j])
    check[i][j] = n
    target = before[i][j]
    temp = after[i][j]
    while Q:
        y, x = Q.popleft()
        if temp != after[y][x]:
            return 2

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or nx < 0 or ny >= N or nx >= M or before[ny][nx] != target or check[ny][nx]: continue
            check[ny][nx] = n
            Q.append([ny, nx])

    if before[i][j] != after[i][j]: return 1
    else: return 0


def answer():
    cnt = 0
    temp = 0
    for i in range(N):
        for j in range(M):
            if not check[i][j]:
                cnt += 1
                temp += bfs(i, j, cnt)
            if temp >= 2:
                return 'NO'

    return 'YES'


print(answer())
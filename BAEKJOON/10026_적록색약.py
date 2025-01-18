import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
grid = [input().split()[0] for _ in range(N)]
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
dic = {'B': 1,
       'R': 2,
       'G': 3}
answer = [0, 0]


def checking(y, x):
    Q = deque()
    Q.append([y, x])
    check[y][x] = dic[grid[y][x]]
    while Q:
        y, x = Q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or nx < 0 or ny >= N or nx >= N or check[ny][nx] or dic[grid[ny][nx]] != check[y][x]: continue
            Q.append([ny, nx])
            check[ny][nx] = dic[grid[ny][nx]]


check = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if check[i][j]: continue
        answer[0] += 1
        checking(i, j)

check = [[0]*N for _ in range(N)]
dic['G'] = 2
for i in range(N):
    for j in range(N):
        if check[i][j]: continue
        answer[1] += 1
        checking(i, j)

print(*answer)
import sys
input = sys.stdin.readline

N = int(input())
sy, sx, ey, ex = map(int, input().split())
dy = [-2, -2, 0, 0, 2, 2]
dx = [-1, 1, -2, 2, -1, 1]

check = [[-1]*N for _ in range(N)]
from collections import deque
Q = deque()
Q.append([sy, sx])
check[sy][sx] = 0

while Q:
    y, x = Q.popleft()
    if y == ey and x == ex: break
    
    for d in range(len(dy)):
        ny = y + dy[d]
        nx = x + dx[d]

        if min(ny, nx) < 0 or max(ny, nx) >= N or check[ny][nx] != -1: continue
        check[ny][nx] = check[y][x] + 1
        Q.append([ny, nx])

print(check[ey][ex])
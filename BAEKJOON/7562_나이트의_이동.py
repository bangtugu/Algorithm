import sys
input = sys.stdin.readline

T = int(input())
dy = [-2, -2, -1, -1, 1, 1, 2, 2]
dx = [-1, 1, -2, 2, -2, 2, -1, 1]

from collections import deque
for _ in range(T):
    N = int(input())
    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())
    check = [[-1]*N for _ in range(N)]
    
    Q = deque()
    check[sy][sx] = 0
    Q.append([sy, sx])
    while Q:
        if check[ey][ex] != -1: break
        y, x = Q.popleft()

        for d in range(8):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or nx < 0 or ny >= N or nx >= N or check[ny][nx] != -1: continue
            check[ny][nx] = check[y][x]+1
            Q.append([ny, nx])
    
    print(check[ey][ex])
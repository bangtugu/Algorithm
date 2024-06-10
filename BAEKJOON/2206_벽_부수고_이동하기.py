import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = 1
table = [input() for _ in range(N)]
check = [[[N*M+5]*(M) for _ in range(N)] for _ in range(K+1)]
check[0][0][0] = 1

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

from collections import deque
Q = deque()
Q.append([0, 0, 0])
while Q:
    k, y, x, = Q.popleft()
    if y == N-1 and x == M-1: break

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        
        if ny < 0 or nx < 0 or ny >= N or nx >= M: continue

        nk = k if table[ny][nx] == '0' else k+1
        if nk > K: continue
        
        if check[k][y][x]+1 < check[nk][ny][nx]:
            check[nk][ny][nx] = check[k][y][x]+1
            Q.append([nk, ny, nx])

answer = [check[i][N-1][M-1] for i in range(K+1)]
if min(answer) == N*M+5:
    print(-1)
else:
    print(min(answer))
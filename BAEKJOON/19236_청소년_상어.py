import sys
input = sys.stdin.readline

dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
pool = [[[0, 0] for _ in range(4)] for _ in range(4)]

for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        pool[i][j] = [line[j*2], line[j*2+1]-1]
from copy import deepcopy


def dfs(value, sy, sx, pool):
    global answer
    value += pool[sy][sx][0]
    pool[sy][sx][0] = 0
    answer = max(answer, value)

    for f in range(1, 17):
        fy, fx, fd = -1, -1, -1
        for i in range(4):
            for j in range(4):
                if pool[i][j][0] == f:
                    fy, fx, fd = i, j, pool[i][j][1]
                    
        if fy == -1: continue
        for d in range(8):
            td = (fd+d)%8
            ty = fy+dy[td]
            tx = fx+dx[td]

            if max(ty, tx) >= 4 or min(ty, tx) < 0 or (ty == sy and tx == sx): continue
            pool[fy][fx][1] = td
            pool[fy][fx], pool[ty][tx] = pool[ty][tx], pool[fy][fx]
            break

    sd = pool[sy][sx][1]
    for i in range(1, 4):
        ny = sy+dy[sd]*i
        nx = sx+dx[sd]*i
        if min(ny, nx) < 0 or max(ny, nx) >= 4: break
        if not pool[ny][nx][0]: continue
        dfs(value, ny, nx, deepcopy(pool))

        
answer = 0
dfs(0, 0, 0, deepcopy(pool))
print(answer)
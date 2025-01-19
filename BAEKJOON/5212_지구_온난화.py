import sys
input = sys.stdin.readline

N, M = map(int, input().split())
now = [input().split()[0] for _ in range(N)]
check = [[0]*M for _ in range(N)]
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
sy, sx, ly, lx = N-1, M-1, 0, 0

for i in range(N):
    for j in range(M):
        if now[i][j] == '.': continue
        for d in range(4):
            y = i + dy[d]
            x = j + dx[d]
            if 0 <= y < N and 0 <= x < M and now[y][x] == 'X':
                check[i][j] += 1
        if check[i][j] <= 1: check[i][j] = 0
        if not check[i][j]: continue
        sy = min(sy, i)
        sx = min(sx, j)
        ly = max(ly, i)
        lx = max(lx, j)

for i in range(sy, ly+1):
    for j in range(sx, lx+1):
        if check[i][j]: print('X', end='')
        else: print('.', end='')
    print()
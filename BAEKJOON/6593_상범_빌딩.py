import sys
input = sys.stdin.readline
from collections import deque

while True:
    L, R, C = map(int, input().split())
    if sum([L, R, C]) == 0: break

    building = []
    check = [[[-1]*C for _ in range(R)]for _ in range(L)]
    Q = deque()
    for z in range(L):
        temp = []
        for y in range(R):
            line = input()
            for x in range(C):
                if line[x] == 'S':
                    Q.append([z, y, x])
                    check[z][y][x] = 0
            temp.append(line)
        
        building.append(temp[:])
        input()

    dz = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dx = [0, 0, 0, 0, 1, -1]

    escape = False
    while Q:
        if escape: break
        z, y, x = Q.popleft()

        for d in range(6):
            nz = z + dz[d]
            ny = y + dy[d]
            nx = x + dx[d]

            if nz < 0 or ny < 0 or nx < 0 or nz >= L or ny >= R or nx >= C: continue
            if check[nz][ny][nx] != -1 or building[nz][ny][nx] == '#': continue

            if building[nz][ny][nx] == 'E':
                escape = check[z][y][x] + 1
                break
            check[nz][ny][nx] = check[z][y][x] + 1
            Q.append([nz, ny, nx])

    if escape:
        print('Escaped in {} minute(s).'.format(escape))
    else:
        print('Trapped!')
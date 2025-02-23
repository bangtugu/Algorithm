import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
mapp = [list(input().split()[0]) for _ in range(N)]
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
ry, rx, by, bx, ey, ex = 0, 0, 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if mapp[i][j] == 'R':
            ry, rx = i, j
            mapp[i][j] = '.'
        if mapp[i][j] == 'B':
            by, bx = i, j
            mapp[i][j] = '.'
        if mapp[i][j] == 'O':
            ey, ex = i, j


def going(ry, rx, by, bx, d):
    s, f = False, False
    while True:
        nry, nrx = [ry + dy[d], rx + dx[d]] if ry != ey or rx != ex else [ry, rx]
        nby, nbx = [by + dy[d], bx + dx[d]] if by != ey or bx != ex else [by, bx]
        if mapp[nry][nrx] == '#' or (mapp[nry][nrx] == '.' and nry == by and nrx == bx): nry, nrx = ry, rx
        if mapp[nby][nbx] == '#' or (mapp[nby][nbx] == '.' and nby == ry and nbx == rx): nby, nbx = by, bx
        if nry == ry and nrx == rx and nby == by and nbx == bx: break
        ry, rx, by, bx = nry, nrx, nby, nbx
    if ey == ry and ex == rx: s = True
    if ey == by and ex == bx: f = True
    return ry, rx, by, bx, s, f


check = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
Q = deque()
Q.append([ry, rx, by, bx, 0])
check[ry][rx][by][bx] = 1
answer = -1
while answer == -1 and Q:
    ry, rx, by, bx, cnt = Q.popleft()

    for d in range(4):
        nry, nrx, nby, nbx, s, f = going(ry, rx, by, bx, d)
        if f: continue
        if s: answer = cnt+1; break
        if check[nry][nrx][nby][nbx]: continue
        check[nry][nrx][nby][nbx] = 1
        Q.append([nry, nrx, nby, nbx, cnt+1])

print(answer)
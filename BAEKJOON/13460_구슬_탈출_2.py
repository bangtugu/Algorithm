dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

from collections import deque


# def play(d, nlst):
#
#     lst = [nlst[i][:] for i in range(N)]
#
#     red = [-1, -1]
#     blue = [-1, -1]
#
#     for i in range(1, N - 1):
#         for j in range(1, M - 1):
#             if lst[i][j] == 'R':
#                 red = [i, j]
#             if lst[i][j] == 'B':
#                 blue = [i, j]
#
#     canmovered = canmoveblue = True
#     finishred = finishblue = False
#
#     while canmovered or canmoveblue:
#
#         if canmovered:
#             nred = [red[0] + dy[d], red[1] + dx[d]]
#
#             if 0 < nred[0] < N - 1 and 0 < nred[1] < M - 1 and lst[nred[0]][nred[1]] != '#':
#                 if lst[nred[0]][nred[1]] == 'B':
#                     canmovered = canmoveblue
#                 elif lst[nred[0]][nred[1]] == 'O':
#                     canmovered = False
#                     finishred = True
#                     lst[red[0]][red[1]] = '.'
#                 else:
#                     lst[red[0]][red[1]] = '.'
#                     lst[nred[0]][nred[1]] = 'R'
#                     red = nred[:]
#             else:
#                 canmovered = False
#
#         if canmoveblue:
#             nblue = [blue[0] + dy[d], blue[1] + dx[d]]
#
#             if 0 < nblue[0] < N - 1 and 0 < nblue[1] < N - 1 and lst[nblue[0]][nblue[1]] != '#':
#                 if lst[nblue[0]][nblue[1]] == 'R':
#                     canmoveblue = canmovered
#                 elif lst[nblue[0]][nblue[1]] == 'O':
#                     canmoveblue = False
#                     finishblue = True
#                     lst[blue[0]][blue[1]] = '.'
#                 else:
#                     lst[blue[0]][blue[1]] = '.'
#                     lst[nblue[0]][nblue[1]] = 'B'
#                     blue = nblue[:]
#             else:
#                 canmoveblue = False
#
#     if finishblue:
#         return False, False, lst
#
#     if finishred:
#         return True, False, lst
#
#     return False, True, lst
#
#
# def bfs():
#
#     Q = deque()
#
#     for i in range(4):
#         Q.append((1, i, table))
#
#     while Q:
#         n, d, lst = Q.popleft()
#         result, process, nlst = play(d, lst)
#
#         if result:
#             return n
#
#         if process:
#             if n+1 == 11:
#                 return -1
#
#             for i in range(4):
#                 Q.append((n+1, i, nlst))
#
#
# N, M = map(int, input().split())
# table = [list(input()) for _ in range(N)]
#
# cnt = bfs()
#
# print(cnt)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

from collections import deque


def play(ry, rx, by, bx, dy, dx):
    rm = 0
    bm = 0
    while table[ry+dy][rx+dx] != '#' and table[ry][rx] != 'O':
        ry += dy
        rx += dx
        rm += 1

    while table[by+dy][bx+dx] != '#' and table[by][bx] != 'O':
        by += dy
        bx += dx
        bm += 1

    return ry, rx, by, bx, rm, bm


def bfs():

    ry = rx = by = bx = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            if table[i][j] == 'R':
                ry, rx = i, j
            if table[i][j] == 'B':
                by, bx = i, j

    v[ry][rx][by][bx] = 1

    Q.append((ry, rx, by, bx, 1))

    while Q:
        ry, rx, by, bx, n = Q.popleft()
        for d in range(4):
            nry, nrx, nby, nbx, rm, bm = play(ry, rx, by, bx, dy[d], dx[d])
            if table[nby][nbx] != 'O':
                if table[nry][nrx] == 'O':
                    return n

                if nry == nby and nrx == nbx:
                    if rm > bm:
                        nry -= dy[d]
                        nrx -= dx[d]
                    else:
                        nby -= dy[d]
                        nbx -= dx[d]

                if not v[nry][nrx][nby][nbx] and n+1 < 11:
                    v[nry][nrx][nby][nbx] = 1
                    Q.append((nry, nrx, nby, nbx, n+1))
    return -1


N, M = map(int, input().split())
table = [list(input()) for _ in range(N)]
v = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
Q = deque()

cnt = bfs()

print(cnt)
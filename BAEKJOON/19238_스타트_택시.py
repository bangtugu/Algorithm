import sys
input = sys.stdin.readline
from collections import deque

N, M, P = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(N)]
y, x = map(int, input().split())
y, x = y-1, x-1
taxi_dic = {}
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]


def move(y1, x1, y2, x2):
    Q = deque()
    check = [[-1]*N for _ in range(N)]
    check[y1][x1] = 0
    Q.append([y1, x1, 0])
    while Q:
        y, x, cnt = Q.popleft()
        if y == y2 and x == x2: return cnt
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny >= N or nx >= N or ny < 0 or nx < 0 or check[ny][nx] != -1 or mapp[ny][nx] == 1: continue
            check[ny][nx] = cnt+1
            Q.append([ny, nx, cnt+1])

    return 0


def path_find(y1, x1):
    Q = deque()
    check = [[-1]*N for _ in range(N)]
    check[y1][x1] = 0
    Q.append([y1, x1, 0])
    lst = []
    while Q:
        y, x, cnt = Q.popleft()
        if mapp[y][x] >= 2: lst.append([y, x, cnt])
        if lst: continue
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny >= N or nx >= N or ny < 0 or nx < 0 or check[ny][nx] != -1 or mapp[ny][nx] == 1: continue
            check[ny][nx] = cnt+1
            Q.append([ny, nx, cnt+1])
    
    if lst:
        lst.sort(key = lambda x: [x[2], x[0], x[1]])
        return lst[0]
    else:
        return -1, -1, -1


can_move = True
for i in range(2, M+2):
    y1, x1, y2, x2 = map(int, input().split())
    y1, x1, y2, x2 = y1-1, x1-1, y2-1, x2-1
    taxi_dic[i] = [y2, x2]
    mapp[y1][x1] = i
    if not move(y1, x1, y2, x2):
        can_move = False

if not can_move:
    print(-1)
else:
    while M:
        y1, x1, v1 = path_find(y, x)
        if y1 == -1: break
        y2, x2 = taxi_dic[mapp[y1][x1]]
        v2 = move(y1, x1, y2, x2)
        if P < v1+v2: break
        P -= v1-v2
        M -= 1
        mapp[y1][x1] = 0
        y, x = y2, x2

    print(P if not M else -1)
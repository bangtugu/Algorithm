import sys
input = sys.stdin.readline
from collections import deque

dy = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
plate = []
for _ in range(5):
    plate.append([[list(map(int, input().split())) for _ in range(5)]])


def path_finding(lst, value):

    if lst[0][0][0] == 0 or lst[4][4][4] == 0: return 0

    visit = [[[0, 0, 0, 0, 0] for _ in range(5)] for _ in range(5)]
    visit[0][0][0] = 1
    Q = deque()
    Q.append([0, 0, 0])

    while Q:
        z, y, x = Q.popleft()
        if visit[z][y][x] == value: return 0

        for d in range(6):
            nz = z + dz[d]
            ny = y + dy[d]
            nx = x + dx[d]

            if nz < 0 or nx < 0 or ny < 0 or nz >= 5 or ny >= 5 or nx >= 5 or lst[nz][ny][nx] == 0 or visit[nz][ny][nx]: continue
            visit[nz][ny][nx] = visit[z][y][x] + 1
            Q.append([nz, ny, nx])
    
    return visit[4][4][4]-1


def roll(lst):
    lst2 = [[0, 0, 0, 0, 0] for _ in range(5)]
    lst3 = [[0, 0, 0, 0, 0] for _ in range(5)]
    lst4 = [[0, 0, 0, 0, 0] for _ in range(5)]

    for y in range(5):
        for x in range(5):
            lst2[x][4-y] = lst[0][y][x]
            lst3[4-y][4-x] = lst[0][y][x]
            lst4[4-x][y] = lst[0][y][x]

    lst.append(lst2)
    lst.append(lst3)
    lst.append(lst4)


def plating(room, check, value):
    if len(room) == 5:
        return path_finding(room, value)

    for i in range(5):
        if check[i]: continue
        check[i] = 1
        for j in range(4):
            now = plating(room+[plate[i][j]], check, value)
            if now == 12:
                return 12
            if now > 12:
                value = min(now, value)
        check[i] = 0

    return value


for i in range(5):
    roll(plate[i])

answer = 5**5
answer = plating([], [0, 0, 0, 0, 0], 5**5)

if answer == 5**5:
    print(-1)
else:
    print(answer)
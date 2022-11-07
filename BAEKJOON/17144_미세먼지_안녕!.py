from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def step1():

    for i in range(R):
        for j in range(C):
            if room[i][j] > 4:
                Q.append([i, j, room[i][j]//5])

    while Q:

        y, x, temp = Q.popleft()

        for i in range(4):

            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < R and 0 <= nx < C and room[ny][nx] != -1:
                room[ny][nx] += temp
                room[y][x] -= temp


def step2_up(y):

    d = 0

    ny = y + dy[d]
    nx = 0

    while True:

        if 0 > nx + dx[d] or nx + dx[d] >= C or y > ny + dy[d] or ny + dy[d] >= R:
            d = (d + 3) % 4

        nny = ny + dy[d]
        nnx = nx + dx[d]

        if room[nny][nnx] == -1:
            room[ny][nx] = 0
            return

        room[ny][nx] = room[nny][nnx]

        ny = nny
        nx = nnx


def step2_down(y):

    d = 2

    ny = y + dy[d]
    nx = 0

    while True:

        if 0 > nx + dx[d] or nx + dx[d] >= C or 0 > ny + dy[d] or ny + dy[d] >= y + 1:
            d = (d + 1) % 4

        nny = ny + dy[d]
        nnx = nx + dx[d]

        if room[nny][nnx] == -1:
            room[ny][nx] = 0
            return

        room[ny][nx] = room[nny][nnx]

        ny = nny
        nx = nnx


R, C, T = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(R)]

my = 0

for i in range(R):
    if room[i][0] == -1:
        my = i
        break

Q = deque()
for _ in range(T):
    step1()
    step2_up(my)
    step2_down(my+1)

ans = 0
for line in room:
    ans += sum(line)

print(ans+2)
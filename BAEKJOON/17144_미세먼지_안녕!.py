dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def step1():
    lst = []
    for i in range(R):
        for j in range(C):
            if room[i][j] > 4:
                lst.append([i, j, room[i][j]//5])

    while lst:

        y, x, temp = lst.pop()

        for i in range(4):

            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < R and 0 <= nx < C and room[ny][nx] != -1:
                room[ny][nx] += temp
                room[y][x] -= temp


def step2_up(y):
    d = 0
    x = 0
    while True:
        ny = y + dy[d]
        nx = x + dx[d]

        if ny < 0 or nx < 0 or ny > my or nx >= C:
            d = (d + 1) % 4
            continue
        
        if room[ny][nx] == -1:
            room[y][x] = 0
            break
        elif room[y][x] != -1:
            room[y][x] = room[ny][nx]

        y = ny
        x = nx


def step2_down(y):

    d = 2
    x = 0

    while True:

        ny = y + dy[d]
        nx = x + dx[d]

        if ny < my+1 or nx < 0 or ny >= R or nx >= C:
            d = (d + 3) % 4
            continue

        if room[ny][nx] == -1:
            room[y][x] = 0
            break
        elif room[y][x] != -1:
            room[y][x] = room[ny][nx]

        y = ny
        x = nx


R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
my = 0
for i in range(R):
    if room[i][0] == -1:
        my = i
        break

for _ in range(T):
    step1()
    step2_up(my)
    step2_down(my+1)

print(sum([sum(line) for line in room])+2)
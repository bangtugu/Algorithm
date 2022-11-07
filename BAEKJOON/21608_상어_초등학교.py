N = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def aroundlike(y, x, n):
    cnt = 0
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]

        if 0 <= yy < N and 0 <= xx < N and table[yy][xx] in students[n][1:]:
            cnt += 1

    return cnt


def step1(n):

    newlst = []
    maxlike = 0

    for i in range(N):
        for j in range(N):
            if table[i][j] == 0:
                nowlike = aroundlike(i, j, n)
                if nowlike > maxlike:
                    maxlike = nowlike
                    newlst = [[i, j]]
                elif nowlike == maxlike:
                    newlst.append([i, j])

    return newlst


def aroundempty(y, x):

    cnt = 0

    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]

        if 0 <= yy < N and 0 <= xx < N and table[yy][xx] == 0:
            cnt += 1

    return cnt


def step2(lst):

    newlst = []
    maxempty = 0

    for chair in lst:
        y = chair[0]
        x = chair[1]

        nowempty = aroundempty(y, x)

        if nowempty > maxempty:
            maxempty = nowempty
            newlst = [[y, x]]
        elif nowempty == maxempty:
            newlst.append([y, x])

    return newlst


def step3(lst):
    for i in range(N):
        for j in range(N):
            if [i, j] in lst:
                return i, j


def calc(y, x):

    now = table[y][x]
    cnt = 0
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        if 0 <= yy < N and 0 <= xx < N and table[yy][xx] in students[now-1][1:]:
            cnt += 1

    if not cnt:
        return 0
    else:
        return 10**(cnt-1)


students = [list(map(int, input().split())) for _ in range(N**2)]

table = [[0]*N for _ in range(N)]

for i in range(N**2):
    step1_list = step1(i)
    if len(step1_list) == 1:
        table[step1_list[0][0]][step1_list[0][1]] = students[i][0]
    else:
        step2_list = step2(step1_list)
        if len(step2_list) == 1:
            table[step2_list[0][0]][step2_list[0][1]] = students[i][0]
        else:
            y, x = step3(step2_list)
            table[y][x] = students[i][0]

students.sort()

happy = 0
for i in range(N):
    for j in range(N):
        happy += calc(i, j)

print(happy)
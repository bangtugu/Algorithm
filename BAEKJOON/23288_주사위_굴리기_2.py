import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
score = [[0]*M for _ in range(N)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]


def set_score(sy, sx):
    score[sy][sx] = 1
    lst = [[sy, sx]]
    idx = 0
    while idx < len(lst):
        y, x = lst[idx]
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or nx < 0 or ny >= N or nx >= M or score[ny][nx] or field[ny][nx] != field[sy][sx]: continue
            score[ny][nx] = 1
            lst.append([ny, nx])
        idx += 1
    
    for y, x in lst:
        score[y][x] = len(lst)*field[sy][sx]


for i in range(N):
    for j in range(M):
        if score[i][j]: continue
        set_score(i, j)


def move(d, dice, y, x):
    ny = y + dy[d]
    nx = x + dx[d]

    if ny < 0 or ny >= N or nx < 0 or nx >= M:
        d = (d+2)%4
        ny = y + dy[d]
        nx = x + dx[d]
    
    y, x = ny, nx
    dice[d], dice[4], dice[5], dice[(d+2)%4] = dice[5], dice[d], dice[(d+2)%4], dice[4]

    if dice[4] > field[y][x]:
        d = (d+1)%4
    elif dice[4] < field[y][x]:
        d = (d+3)%4

    return score[y][x], d, dice, y, x


answer = 0
d = 0
dice = [3, 5, 4, 2, 6, 1]
y, x = 0, 0
for _ in range(K):
    s, d, dice, y, x = move(d, dice, y, x)
    answer += s

print(answer)
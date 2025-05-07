import sys
input = sys.stdin.readline

table = [list(map(int, input().split())) for _ in range(19)]
winner = 0
win_stone = [0, 0]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]


def checking(y, x):
    lst = [0]*8

    for d in range(8):
        cnt = 0
        ny = y + dy[d]
        nx = x + dx[d]
        while min(ny, nx) >= 0 and max(ny, nx) < 19 and table[y][x] == table[ny][nx]:
            cnt += 1
            ny += dy[d]
            nx += dx[d]
        lst[d] += cnt

    for i in range(4):
        if lst[i]+lst[i+4] != 4: continue
        stone = [0, 0]

        if i == 0:
            stone = [y-lst[0]+1, x-lst[0]+1]
        elif i == 1:
            stone = [y-lst[1]+1, x+1]
        elif i == 2:
            stone = [y+lst[6]+1, x-lst[6]+1]
        else:
            stone = [y+1, x-lst[7]+1]

        return table[y][x], stone
    return 0, [0, 0]


for i in range(19):
    if winner: break
    for j in range(19):
        if winner: break
        if not table[i][j]: continue
        winner, win_stone = checking(i, j)


print(winner)
if winner: print(*win_stone)
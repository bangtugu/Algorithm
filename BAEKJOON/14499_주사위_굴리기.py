dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

dice = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}

row = [6, 3, 1, 4]
col = [6, 5, 1, 2]

N, M, y, x, K = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]

rollst = list(map(int, input().split()))

for roll in rollst:
    if 0 <= y + dy[roll] < N and 0 <= x + dx[roll] < M:

        y += dy[roll]
        x += dx[roll]

        if roll == 1:
            row = row[1:] + [row[0]]
            col[0], col[2] = row[0], row[2]
        elif roll == 2:
            row = [row[-1]] + row[:-1]
            col[0], col[2] = row[0], row[2]
        elif roll == 3:
            col = [col[-1]] + col[:-1]
            row[0], row[2] = col[0], col[2]
        elif roll == 4:
            col = col[1:] + [col[0]]
            row[0], row[2] = col[0], col[2]

        if table[y][x] == 0:
            table[y][x] = dice[col[0]]
        else:
            dice[col[0]] = table[y][x]
            table[y][x] = 0

        # print(row)
        # print(col)
        # print()

        print(dice[col[2]])
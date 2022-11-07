dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


N, M = map(int, input().split())
y, x, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

cleaning = True
clean_cnt = 0
turn_cnt = 0

while cleaning:

    if not room[y][x]:
        room[y][x] = 2
        clean_cnt += 1

    while True:

        d = (d + 3) % 4

        left_y = y + dy[d]
        left_x = x + dx[d]

        if not room[left_y][left_x]:
            y = left_y
            x = left_x
            turn_cnt = 0
            break
        else:
            turn_cnt += 1

        if turn_cnt >= 4:

            back_y = y - dy[d]
            back_x = x - dx[d]

            if room[back_y][back_x] == 1:
                cleaning = False
                break
            else:
                y = back_y
                x = back_x
                turn_cnt = 0

print(clean_cnt)
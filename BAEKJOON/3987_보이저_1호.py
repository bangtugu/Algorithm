di = ['U', 'R', 'D', 'L']
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
space = [input() for _ in range(N)]
PR, PC = map(int, input().split())
PR -= 1
PC -= 1

max_signal = 0
max_d = ''

for i in range(4):

    signal = 0
    y = PR
    x = PC
    d = i

    while True:
        y = y + dy[d]
        x = x + dx[d]
        signal += 1

        if 0 > y or y >= N or 0 > x or x >= M or space[y][x] == 'C':
            if signal > max_signal:
                max_signal = signal
                max_d = di[i]
            break

        if space[y][x] == '/':
            if d % 2:
                d = d - 1
            else:
                d = d + 1
        elif space[y][x] == '\\':
            if d % 2:
                d = (d + 1) % 4
            else:
                d = 3 - d

        if [y, x, d] == [PR, PC, i]:
            max_signal = 'Voyager'
            max_d = di[i]
            break

    if max_signal == 'Voyager':
        break

print(max_d)
print(max_signal)
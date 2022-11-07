from collections import deque

N = int(input())
K = int(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

table = [[0]*N for _ in range(N)]

snake = deque()
snake.append((0, 0))
d = 1

for _ in range(K):
    ay, ax = map(int, input().split())
    table[ay-1][ax-1] = 'A'

L = int(input())

turn = {}
for _ in range(L):
    k, v = input().split()
    turn[int(k)] = v

play = True
time = 0
turncnt = 0
hy = hx = 0

while play:

    time += 1
    hy, hx = hy + dy[d], hx + dx[d]
    if 0 <= hy < N and 0 <= hx < N and (hy, hx) not in snake:
        snake.append((hy, hx))
        if table[hy][hx] == 'A':
            table[hy][hx] = 0
        else:
            snake.popleft()
    else:
        break

    if time in turn.keys():
        if turn[time] == 'L':
            d = (d + 3) % 4
        elif turn[time] == 'D':
            d = (d + 1) % 4

print(time)
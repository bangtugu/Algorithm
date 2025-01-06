import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
field = [[0]*C for _ in range(R)]
field1 = [[1]*C for _ in range(R)]
field2 = [[1]*C for _ in range(R)]
field3 = [[1]*C for _ in range(R)]
dy = [0, 0, 0, 1, -1]
dx = [0, 1, -1, 0, 0]

for i in range(R):
    line = input()
    for j in range(C):
        if line[j] == 'O':
            field[i][j] = 1
            for d in range(5):
                y = i + dy[d]
                x = j + dx[d]
                if y < 0 or x < 0 or y >= R or x >= C: continue
                field1[y][x] = 0

for i in range(R):
    for j in range(C):
        if field1[i][j] == 1:
            for d in range(5):
                y = i + dy[d]
                x = j + dx[d]
                if y < 0 or x < 0 or y >= R or x >= C: continue
                field2[y][x] = 0

if not N%2: target = field3
elif (N//2)%2: target = field1
else: target = field2
if N == 1: target = field

for line in target:
    for a in line:
        if a == 0:
            print('.', end = '')
        else:
            print('O', end = '')
    print()
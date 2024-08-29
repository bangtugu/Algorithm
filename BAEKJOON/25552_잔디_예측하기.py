import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
start = [list(input()) for _ in range(N)]
D = int(input())
end = [list(input()) for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

check = [[0]*M for _ in range(N)]
Q = deque()

for i in range(N):
    for j in range(M):
        if start[i][j] == 'O':
            check[i][j] = 1
            Q.append([i, j])

while Q:
    y, x = Q.popleft()

    ys, ye = max(0, y-D), min(y+D+1, N)

    for i in range(ys, ye):
        for j in range(max(0, x-D+abs(y-i)), min(x+D-abs(y-i)+1, M)):
            if check[i][j] or end[i][j] == 'X': continue
            check[i][j] = 1
            Q.append([i, j])

cannot = False
for i in range(N):
    for j in range(M):
        if start[i][j] == 'O' and end[i][j] != 'O':
            cannot = True
            break
        if end[i][j] == 'O' and not check[i][j]:
            cannot = True
            break
    if cannot: break

if cannot:
    print('NO')
else:
    print('YES')



'''
python3 시간초과
pypy3 틀렷습니다?

'''
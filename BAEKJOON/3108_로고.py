import sys
input = sys.stdin.readline

N = int(input())

table = [[[] for _ in range(1001)] for _ in range(1001)]
check = [[0]*1001 for _ in range(1001)]
max
for i in range(1, N+1):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 500
    y1 += 500
    x2 += 500
    y2 += 500

    for j in range(x1, x2+1):
        if not table[j][y1]: table[j][y1] = set()
        if not table[j][y2]: table[j][y2] = set()
        table[j][y1].add(i)
        table[j][y2].add(i)
    
    for j in range(y1, y2+1):
        if not table[x1][j]: table[x1][j] = set()
        if not table[x2][j]: table[x2][j] = set()
        table[x1][j].add(i)
        table[x2][j].add(i)

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
group = [-1]*(N+1)
from collections import deque
cnt = 0
for i in range(1001):
    for j in range(1001):
        if not table[i][j] or check[i][j]: continue
        cnt += 1
        check[i][j] = 1
        square_set = set()
        square_set = square_set.union(table[i][j])
        Q = deque()
        Q.append([i, j])
        while Q:
            y, x = Q.popleft()

            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if ny < 0 or nx < 0 or nx >= 1001 or ny >= 1001 or not table[ny][nx] or check[ny][nx]: continue
                if not (table[ny][nx] & square_set): continue
                square_set = square_set.union(table[ny][nx])
                check[ny][nx] = 1
                Q.append([ny, nx])

print(cnt if not table[500][500] else cnt-1)
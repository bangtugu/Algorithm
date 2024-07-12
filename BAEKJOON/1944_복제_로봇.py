import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mapp = [input() for _ in range(N)]

table = [[-1]*N for _ in range(N)]
spot = [[0, 0] for _ in range(M+1)]

cnt = 1
for i in range(N):
    for j in range(N):
        if mapp[i][j] == 'S':
            table[i][j] = 0
            spot[0] = [i, j]
        elif mapp[i][j] == 'K':
            table[i][j] = cnt
            spot[cnt] = [i, j]
            cnt += 1

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
from collections import deque
distance = [[0]*(M+1) for _ in range(M+1)]
for i in range(M):
    check = [[-1]*N for _ in range(N)]
    y, x = spot[i]
    Q = deque()
    Q.append([y, x])
    check[y][x] = 0
    while Q:
        y, x = Q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or nx < 0 or ny >= N or nx >= N or mapp[ny][nx] == '1' or check[ny][nx] != -1: continue
            check[ny][nx] = check[y][x] + 1
            Q.append([ny, nx])
            if table[ny][nx] != -1: 
                distance[i][table[ny][nx]] = check[ny][nx]
                distance[table[ny][nx]][i] = check[ny][nx]
    
min_distance = []
for i in range(M+1):
    line = list(range(M+1))
    line.sort(key = lambda x: distance[i][x])
    min_distance.append(line)


def dfs(check, value):
    if sum(check) == M+1:
        return value

    min_next = [0, 0, N*N]
    for s in range(M+1):
        if not check[s]: continue
        for n in min_distance[s]:
            if check[n]: continue
            if distance[s][n] < min_next[2]:
                min_next = [s, n, distance[s][n]]
            break

    check[min_next[1]] = 1
    return dfs(check, value+min_next[2])


for i in range(1, M+1):
    if distance[0][i] == 0:
        print(-1)
        break
else:
    print(dfs([1]+[0]*M, 0))



'''

5 2
11111
1S001
10001
1K1K1
11111


4 1
1111
1S11
11K1
1111

'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

room = []
for _ in range(M):
    room.append(list(input())[:N])

spot = {}
cnt = 1
for i in range(M):
    for j in range(N):
        if room[i][j] == 'X':
            spot[cnt] = [i, j]
            room[i][j] = cnt
            cnt += 1
        elif room[i][j] == 'S':
            spot[0] = [i, j]
            room[i][j] = 0
        elif room[i][j] == 'E':
            spot['E'] = [i, j]

spot[cnt] = spot['E']
room[spot[cnt][0]][spot[cnt][1]] = cnt
cnt += 1

cost = [[N*M]*cnt for _ in range(cnt)]
from collections import deque
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
for s in range(cnt):
    Q = deque()
    Q.append(spot[s])
    check = [[-1]*N for _ in range(M)]
    check[spot[s][0]][spot[s][1]] = 0
    while Q:
        y, x = Q.popleft()
        
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or ny >= M or nx < 0 or nx >= N or check[ny][nx] != -1 or room[ny][nx] == '#': continue

            check[ny][nx] = check[y][x]+1
            Q.append([ny, nx])

            if type(room[ny][nx]) == type(0) and room[ny][nx] > s:
                cost[s][room[ny][nx]] = check[ny][nx]
                cost[room[ny][nx]][s] = check[ny][nx]


def path_finding(now, value, check):

    if sum(check) == cnt-1:
        return value + cost[now][-1]

    min_value = N*M
    for i in range(1, cnt-1):
        if check[i]: continue

        check[i] = 1
        min_value = min(min_value, path_finding(i, value+cost[now][i], check))
        check[i] = 0
    
    return min_value


print(path_finding(0, 0, [1]+[0]*(cnt-2)))
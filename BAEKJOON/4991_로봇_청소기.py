import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]


def move(y1, x1, y2, x2):
    check = [[-1]*M for _ in range(N)]
    Q = deque()
    Q.append([y1, x1, 0])
    while Q:
        y, x, c = Q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny == y2 and nx == x2: return c+1
            if ny < 0 or nx < 0 or ny >= N or nx >= M or check[ny][nx] != -1 or mapp[ny][nx] == 'x': continue
            check[ny][nx] = c+1
            Q.append([ny, nx, c+1])
            
    return -1


def dfs(now, v):
    if sum(check) == len(lst):
        return v
    
    value = N*M*len(lst)
    for i in range(len(lst)):
        if check[i]: continue
        check[i] = 1
        value = min(value, dfs(i, v+cost[now][i]))
        check[i] = 0
    
    return value


while M+N:
    answer = 0
    mapp = []
    for _ in range(N):
        mapp.append(input().split()[0])
    
    lst = [[0, 0]]
    for i in range(N):
        for j in range(M):
            if mapp[i][j] == '*':
                lst.append([i, j])
            elif mapp[i][j] == 'o':
                lst[0] = [i, j]
    
    cost = [[-1]*len(lst) for _ in range(len(lst))]
    for i in range(len(lst)):
        cost[i][i] = 0
        for j in range(i+1, len(lst)):
            c = move(lst[i][0], lst[i][1], lst[j][0], lst[j][1])
            cost[i][j] = c
            cost[j][i] = c
    
    for line in cost:
        answer = min(line)
        if answer <= -1: break
    else:
        temp = [-1]*len(lst)
        check = [0]*len(lst)
        check[0] = 1
        answer = dfs(0, 0)

    print(answer)
    M, N = map(int, input().split())
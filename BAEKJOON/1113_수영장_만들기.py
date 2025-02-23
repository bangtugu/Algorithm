import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
pool = [list(map(int, list(input().split()[0]))) for _ in range(N)]
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
answer = 0


def bfs(y, x):
    check = [[0]*M for _ in range(N)]
    check[y][x] = 1
    lst = [[y, x]]
    h = pool[y][x]
    target_h = 10

    idx = 0
    while idx < len(lst):
        y, x = lst[idx]
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or nx < 0 or ny >= N or nx >= M: return
            
            if not check[ny][nx] and h >= pool[ny][nx]:
                lst.append([ny, nx])
                check[ny][nx] = 1
            elif h < pool[ny][nx]:
                target_h = min(target_h, pool[ny][nx])
        idx += 1
    
    global answer
    for y, x in lst:
        answer += target_h - pool[y][x]
        pool[y][x] = target_h


for i in range(1, N-1):
    for j in range(1, M-1):
        bfs(i, j)

print(answer)
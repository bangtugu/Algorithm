import sys
input = sys.stdin.readline

N = int(input())


def setting(y, x, c):
    for z in range(y, N):
        check[z][x] += c
    for z in range(1, N):
        if y+z < N and x+z < N:
            check[y+z][x+z] += c
        if y+z < N and x-z >= 0:
            check[y+z][x-z] += c


def dfs(y):
    if y >= N:
        return 1
    
    temp = 0
    for j in range(N):
        if check[y][j]: continue
        setting(y, j, 1)
        temp += dfs(y+1)
        setting(y, j, -1)

    return temp


check = [[0]*N for _ in range(N)]
answer = dfs(0)

print(answer)
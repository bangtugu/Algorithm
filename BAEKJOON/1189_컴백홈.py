import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
field = [input() for _ in range(R)]
check = [[0]*C for _ in range(R)]
check[R-1][0] = 1
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def dfs(y, x):
    if check[y][x] == K:
        if y == 0 and x == C-1:
            global answer
            answer += 1
        return
    
    if y == 0 and x == C-1: return
    
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if ny < 0 or nx < 0 or ny >= R or nx >= C or check[ny][nx] or field[ny][nx] == 'T': continue
        check[ny][nx] = check[y][x]+1
        dfs(ny, nx)
        check[ny][nx] = 0
    

answer = 0
dfs(R-1, 0)
print(answer)
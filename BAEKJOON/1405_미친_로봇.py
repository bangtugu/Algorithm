import sys
input = sys.stdin.readline

N, ea, we, so, no = map(int, input().split())
p = [ea, we, so, no]
check = [[0]*(N*2+1) for _ in range(N*2+1)]
check[N][N] = 1
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
temp = 0


def dfs(y, x, n, cnt):
    if not cnt: return
    if n == N:
        global temp
        temp += cnt
        return
    
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if check[ny][nx] or not p[d]: continue
        check[ny][nx] = 1
        dfs(ny, nx, n+1, cnt*p[d])
        check[ny][nx] = 0


dfs(N, N, 0, 1)
print(temp/100**N)
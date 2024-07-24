import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

mapp = [input() for _ in range(N)]
target = input().split()[0]
T = len(target)
dp = [[[-1]*T for _ in range(M)] for _ in range(N)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def dfs(y, x, cnt):

    if cnt == T-1:
        return 1

    val = 0
    for d in range(4):
        for c in range(1, K+1):
            ny = y + dy[d]*c
            nx = x + dx[d]*c

            if ny < 0 or ny >= N or nx < 0 or nx >= M: break
            if mapp[ny][nx] != target[cnt+1]: continue
            if dp[ny][nx][cnt+1] != -1:
                val += dp[ny][nx][cnt+1]
            else:
                val += dfs(ny, nx, cnt+1)

    dp[y][x][cnt] = val

    return val


answer = 0
for i in range(N):
    for j in range(M):
        if mapp[i][j] == target[0]:
            answer += dfs(i, j, 0)
print(answer)


'''

4 4 1
KAKT
XEAS
YRWU
ZBQP
BREAK

'''
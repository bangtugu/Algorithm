import sys
input = sys.stdin.readline

N, T = map(int, input().split())
lst = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
lst.sort(key = lambda x: x[0])

dp = [[0]*(T+1) for _ in range(N+1)]

for i in range(1, N+1):
    t, s = lst[i]

    for j in range(1, T+1):
        if j >= t:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-t]+s)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][T])
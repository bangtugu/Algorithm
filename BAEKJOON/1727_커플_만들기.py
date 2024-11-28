import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nlst = sorted(list(map(int, input().split())))
mlst = sorted(list(map(int, input().split())))

dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j-1] + abs(nlst[i-1] - mlst[j-1])
        if i > j:
            dp[i][j] = min(dp[i][j], dp[i-1][j])
        if j > i:
            dp[i][j] = min(dp[i][j], dp[i][j-1])

print(dp[-1][-1])
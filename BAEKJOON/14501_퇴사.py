N = int(input())

work = []

dp = [0] * (N+1)

for i in range(N):
    d, p = map(int, input().split())
    work.append([i+d, p])

for i in range(N-1, -1, -1):
    if work[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(work[i][1] + dp[work[i][0]], dp[i+1])

print(dp[0])
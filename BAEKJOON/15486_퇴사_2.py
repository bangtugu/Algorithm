import sys
input = sys.stdin.readline

N = int(input())
lst = [0]+[list(map(int, input().split())) for _ in range(N)]
dp = [0]*(N+1)

for i in range(1, N+1):
    if i + lst[i][0] - 1 <= N:
        dp[i+lst[i][0]-1] = max(dp[i+lst[i][0]-1], dp[i-1] + lst[i][1])
    
    dp[i] = max(dp[i], dp[i-1])

print(max(dp[N], dp[N-1]))
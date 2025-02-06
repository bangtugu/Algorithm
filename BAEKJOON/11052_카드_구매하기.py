import sys
input = sys.stdin.readline

N = int(input())
lst = [0] + list(map(int, input().split()))

dp = lst[:]

for i in range(1, N+1):
    for j in range(i):
        dp[i] = max(dp[i], dp[i-j]+dp[j])

print(dp[N])
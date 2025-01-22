import sys
input = sys.stdin.readline

D, K = map(int, input().split())
dp = [[0, 0] for _ in range(D+1)]
dp[1] = [1, 0]
dp[2] = [0, 1]

for i in range(3, D+1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for i in range(1, K+1):
    if not (K-dp[D][0]*i)%dp[D][1]:
        print(i)
        print((K-dp[D][0]*i)//dp[D][1])
        break
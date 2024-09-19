# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# lst = [list(map(int, input().split())) for _ in range(N)]

# dp = [[0]*(K+1) for _ in range(N+1)]

# for i in range(1, N+1):
#     for j in range(1, K+1):
#         if lst[i-1][0] > j:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(lst[i-1][1] + dp[i-1][j-lst[i-1][0]], dp[i-1][j])

# print(dp[N][K])


import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
dp = [0]*(K+1)

for W, V in lst:
    
    for i in range(K, W-1, -1):
        dp[i] = max(dp[i], dp[i-W]+V)

print(dp[K])
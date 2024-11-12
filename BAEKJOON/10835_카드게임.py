import sys
input = sys.stdin.readline

N = int(input())
left = list(map(int, input().split()))
right = list(map(int, input().split()))

if max(left) > max(right):
    print(sum(right))
else:
    dp = [[-1]*(N+1) for _ in range(N+1)]
    dp[0][0] = 0

    for l in range(N):
        for r in range(N):
            if dp[l][r] == -1: continue
            if left[l] > right[r]:
                dp[l][r+1] = max(dp[l][r+1], dp[l][r] + right[r])
            dp[l+1][r+1] = max(dp[l+1][r+1], dp[l][r])
            dp[l+1][r] = max(dp[l+1][r], dp[l][r])
    
    answer = max(dp[-1]+[dp[i][-1] for i in range(N+1)])
    print(answer)
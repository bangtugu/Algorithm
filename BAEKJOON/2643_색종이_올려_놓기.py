import sys
input = sys.stdin.readline

N = int(input())
lst = [[1000, 1000]]
for _ in range(N):
    y, x = map(int, input().split())
    lst.append([max(y, x), min(y, x)])

lst.sort(reverse=True)
answer = 0
dp = [[0, lst[i][1]] for i in range(N+1)]
for i in range(1, N+1):
    for j in range(i-1, -1, -1):
        if dp[j][1] >= lst[i][1] and dp[j][0] + 1 > dp[i][0]:
            dp[i][0] = dp[j][0] + 1
            dp[i][1] = lst[i][1]
            answer = max(answer, dp[i][0])

print(answer)
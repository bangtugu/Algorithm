import sys
input = sys.stdin.readline


'''

1: 10000
3: 25000 / 1
5: 37000 / 2

'''

N, M = map(int, input().split())
cannot = set()
if M: cannot = set(map(int, input().split()))

dp = [[0]*(N+5) for _ in range(N+5)]


def dfs(day, coupon):
    if day > N:
        return 0
    
    if dp[day][coupon]:
        return dp[day][coupon]

    if day in cannot:
        dp[day][coupon] = dfs(day+1, coupon)
        return dp[day][coupon]

    dp[day][coupon] = min(dfs(day+1, coupon)+10000,
                          dfs(day+3, coupon+1)+25000,
                          dfs(day+5, coupon+2)+37000)
    
    if coupon >= 3:
        dp[day][coupon] = min(dfs(day+1, coupon-3), dp[day][coupon])

    return dp[day][coupon]


print(dfs(1, 0))


    



# def check(day, cost, coupon):
#     print(day)
#     if day >= N:
#         return cost

#     if visit[day]:

#         cp = check(day+1, cost, coupon-3) if coupon >= 3 else N*10000
#         p1 = check(day+1, cost+10000, coupon)
#         p3 = check(day+3, cost+25000, coupon+1)
#         p5 = check(day+5, cost+37000, coupon+2)

#         min_cost = min(cp, p1, p3, p5)

#     else:
#         min_cost = check(day+1, cost, coupon)


#     return min_cost

# answer = check(0, 0, 0)

# print(dp[-1][0])
# import sys
# input = sys.stdin.readline

# N = int(input())
# W = int(input())

# issues = [list(map(int, input().split())) for _ in range(W)]
# dp = [[[1, 1, N, N, 0], [1, 1, N, N, 0]] for _ in range(W+1)]

# for i in range(1, W+1):
#     ty, tx = issues[i-1]
#     y11, x11, y12, x12, v1 = dp[i-1][0]
#     y21, x21, y22, x22, v2 = dp[i-1][1]

#     if v1 + abs(y11-ty) + abs(x11-tx) < v2 + abs(y21-ty) + abs(x21-tx):
#         dp[i][0] = [ty, tx, y12, x12, v1 + abs(y11-ty) + abs(x11-tx)]
#     else:
#         dp[i][0] = [ty, tx, y22, x22, v2 + abs(y21-ty) + abs(x21-tx)]
    
#     if v1 + abs(y12-ty) + abs(x12-tx) < v2 + abs(y22-ty) + abs(x22-tx):
#         dp[i][1] = [y11, x11, ty, tx, v1 + abs(y12-ty) + abs(x12-tx)]
#     else:
#         dp[i][1] = [y21, x21, ty, tx, v2 + abs(y22-ty) + abs(x22-tx)]

# print(min(dp[-1][0][-1], dp[-1][1][-1]))
# lst = []
# if dp[-1][0][-1] < dp[-1][1][-1]:
#     temp = dp[-1][0][:4]
# else:
#     temp = dp[-1][1][:4]

# for i in range(W-1, -1, -1):
#     ty, tx = issues[i]
#     y1, x1, y2, x2 = temp

#     if y1 == ty and x1 == tx:
#         lst.append(1)
#         if dp[i][0][2] == y2 and dp[i][0][3] == x2:
#             temp = dp[i][0][:4]
#         else:
#             temp = dp[i][1][:4]
#     else:
#         lst.append(2)
#         if dp[i][0][0] == y1 and dp[i][0][1] == x1:
#             temp = dp[i][0][:4]
#         else:
#             temp = dp[i][1][:4]

# for n in reversed(lst):
#     print(n)


import sys
input = sys.stdin.readline
sys.setrecursionlimit(1100)

N = int(input())
W = int(input())
max_val = N*2*W

issues = [[1, 1], [N, N]] + [list(map(int, input().split())) for _ in range(W)]
dist = [[0]*(W+2) for _ in range(W+2)]
dp = [[-1]*(W+2) for _ in range(W+2)]
tracker = [[0]*(W+2) for _ in range(W+2)]


def get_dist(n1, n2):
    y1, x1, y2, x2 = issues[n1] + issues[n2]
    return abs(y1 - y2) + abs(x1 - x2)


for i in range(W+2):
    for j in range(i+1, W+2):
        value = get_dist(i, j)
        dist[i][j] = value
        dist[j][i] = value


def going_out(c1, c2):
    t = max(c1, c2)+1
    if t == W+2: return 0
    if dp[c1][c2] != -1: return dp[c1][c2]

    case1 = going_out(t, c2) + dist[c1][t]
    case2 = going_out(c1, t) + dist[c2][t]
    if case1 < case2:
        dp[c1][c2] = case1
        tracker[c1][c2] = 1
    else:
        dp[c1][c2] = case2
        tracker[c1][c2] = 2
    
    return dp[c1][c2]


print(going_out(0, 1))
c1, c2 = 0, 1
for i in range(2, W+2):
    print(tracker[c1][c2])
    if tracker[c1][c2] == 1:
        c1 = i
    else:
        c2 = i
# from collections import deque
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
#
# def check(y, x):
#
#     v = [[0]*N for _ in range(N)]
#     Q = deque()
#     Q.append((y, x, 0))
#
#     while Q:
#
#         y, x, n = Q.popleft()
#
#         for i in range(4):
#
#             ny = y + dy[i]
#             nx = x + dx[i]
#
#             if 0 <= ny < N and 0 <= nx < N and not v[ny][nx]:
#                 if city[ny][nx] == 2:
#                     return n+1
#                 v[ny][nx] = 1
#                 Q.append((ny, nx, n+1))
#
#
# def dfs(n, y, x):
#
#     if n == 0:
#         global ans
#         new_ans = 0
#         for i in range(N):
#             for j in range(N):
#                 if city[i][j] == 1:
#                     new_ans += check(i, j)
#                 if new_ans >= ans:
#                     return
#
#         ans = min(ans, new_ans)
#         return
#
#     for i in range(y, N):
#         if i != y:
#             x = 0
#         for j in range(x, N):
#             if city[i][j] == 2:
#                 city[i][j] = 0
#                 dfs(n-1, i, j)
#                 city[i][j] = 2
#
#
# N, M = map(int, input().split())
# city = [list(map(int, input().split())) for _ in range(N)]
#
# ans = 500000
#
# origin_chicken = 0
#
# for line in city:
#     origin_chicken += line.count(2)
#
# M = origin_chicken - M
#
# dfs(M, 0, 0)
#
# print(ans)

'''
dfs, bfs
시간초과
'''


from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

homes = []
chickens = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append([i, j])                            # 집, 치킨집 각 배열에 저장
        elif city[i][j] == 2:
            chickens.append([i, j])

ans = 4*N*N

for chicken in combinations(chickens, M):                   # 모든 치킨집 조합에 대해서
    new_ans = 0
    for home in homes:                                      # 각 집마다
        low_dis = 2*N
        for i in range(M):                                  # 각 치킨집에 대해서
            low_dis = min(low_dis, abs(home[0]-chicken[i][0]) + abs(home[1]-chicken[i][1]))         # 치킨 거리 계산
        new_ans += low_dis
    ans = min(ans, new_ans)

print(ans)
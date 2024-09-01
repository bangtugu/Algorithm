# import sys
# input = sys.stdin.readline
# import heapq

# N, M = map(int, input().split())
# cost = [[10001*N]*N for _ in range(N)]

# loop = False
# for _ in range(M):
#     A, B, C = map(int, input().split())
#     if A == B and C < 0: loop = True; break
#     cost[A-1][B-1] = min(cost[A-1][B-1], C)
# for i in range(N):
#     cost[i][i] = 0

# lst = []
# for i in range(1, N):
#     if cost[0][i] == 10001*N: continue
#     heapq.heappush(lst, [cost[0][i], i])

# while lst:
#     if loop: break
#     if cost[0][0] < 0: loop = True; break
#     v, now = heapq.heappop(lst)
#     if v > cost[0][now]: continue

#     for i in range(N):
#         if cost[now][i] == 10001*N: continue
#         if cost[0][i] > v + cost[now][i]:
#             cost[0][i] = v + cost[now][i]
#             heapq.heappush(lst, [cost[0][i], i])

#         if cost[0][i] + cost[i][0] < 0: loop = True; break

# if loop:
#     print(-1)
# else:
#     for i in range(1, N):
#         print(cost[0][i] if cost[0][i] != 10001*N else -1)


# '''
# 45% 시간초과
# '''


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
max_v = N*10001
lst = []
for _ in range(M):
    a, b, c = map(int, input().split())
    lst.append([a-1, b-1, c])

min_dist = [0]+[max_v]*(N-1)
loop = False

for i in range(N):

    for now, next, cost in lst:
        if min_dist[now] == max_v: continue
        if min_dist[next] <= min_dist[now] + cost: continue

        min_dist[next] = min_dist[now] + cost
        if i == N-1: loop = True

if loop:
    print(-1)
else:
    for i in range(1, N):
        print(min_dist[i] if min_dist[i] != max_v else -1)
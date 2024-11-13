import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N, M, K = map(int, input().split())
roads = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    roads[a].append([b, c])
    roads[b].append([a, c])
inf = 1000000*N
dp = [[inf]*(K+1) for _ in range(N+1)]

answer = 1000000*N
HQ = [[0, 1, 0]]
while HQ:
    cost, now, nowk = heappop(HQ)
    if dp[now][nowk] < cost: continue

    for b, c in roads[now]:
        if nowk < K and cost < dp[b][nowk+1]:
            dp[b][nowk+1] = cost
            heappush(HQ, [cost, b, nowk+1])

        if cost + c < dp[b][nowk]:
            dp[b][nowk] = cost + c
            heappush(HQ, [cost+c, b, nowk])

print(min(dp[N]))
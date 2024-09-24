import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
M = int(input())
cost = [[-1]*N for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    if cost[a-1][b-1] == -1:
        cost[a-1][b-1] = c
    else:
        cost[a-1][b-1] = min(c, cost[a-1][b-1])

s, e = map(int, input().split())
HQ = [[0, s-1, [s-1]]]
dist = [-1]*N
while HQ:
    c, now, lst = heappop(HQ)

    if now == e-1:
        for i in range(len(lst)):
            lst[i] += 1
        print(c)
        print(len(lst))
        print(*lst)
        break

    for i in range(N):
        if i == now or i == s-1 or cost[now][i] == -1: continue
        if dist[i] == -1 or dist[i] > c + cost[now][i]:
            dist[i] = c + cost[now][i]
            heappush(HQ, [dist[i], i, lst+[i]])
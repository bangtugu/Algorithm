import sys
input = sys.stdin.readline

N, M = map(int, input().split())
roads = [{} for _ in range(N+1)]
check = [-1]*(N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    if b not in roads[a]:
        roads[a][b] = c
        roads[b][a] = c
    else:
        roads[a][b] = min(roads[a][b], c)
        roads[b][a] = min(roads[b][a], c)

from heapq import heappush, heappop
HQ = [[0, 1]]
check[1] = 0
while HQ:
    cost, now = heappop(HQ)
    if cost > check[now]: continue

    for next in roads[now]:
        if check[next] == -1 or check[next] > cost + roads[now][next]:
            check[next] = cost + roads[now][next]
            heappush(HQ, [check[next], next])

print(check[N])
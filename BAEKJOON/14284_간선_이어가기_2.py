import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N, M = map(int, input().split())
node = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    node[a].append([b, c])
    node[b].append([a, c])

check = [-1]*(N+1)
s, t = map(int, input().split())
check[s] = 0

HQ = [[0, s]]
while HQ:
    cost, now = heappop(HQ)
    if cost < check[now]: continue
    if now == t: break

    for n, c in node[now]:
        if check[n] == -1 or check[n] > cost + c:
            check[n] = cost + c
            heappush(HQ, [check[n], n])

print(check[t])
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())-1

road = {}

for _ in range(E):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1

    if u in road:
        if v in road[u]:
            road[u][v] = min(w, road[u][v])
        else:
            road[u][v] = w
    else:
        road[u] = {v : w}

answer = ['INF']*V
answer[K] = 0
from heapq import heappop, heappush
HQ = [[0, K]]

while HQ:
    cost, now = heappop(HQ)
    if cost > answer[now]: continue
    if now not in road: continue

    for i in road[now]:
        if answer[i] == 'INF' or cost + road[now][i] < answer[i]:
            answer[i] = cost + road[now][i]
            heappush(HQ, [answer[i], i])

for i in range(V):
    print(answer[i])

'''

5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6



0
2
3
7
INF

'''
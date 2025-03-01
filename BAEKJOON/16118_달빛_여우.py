import sys
input = sys.stdin.readline

N, M = map(int, input().split())
roads = [[] for _ in range(N)]
maxv = 10**11
for _ in range(M):
    a, b, c = map(int, input().split())
    roads[a-1].append([b-1, c])
    roads[b-1].append([a-1, c])

from heapq import heappush, heappop
fox = [maxv]*N
HQ = [(0, 0)]
while HQ:
    d, now = heappop(HQ)
    if fox[now] < d: continue

    for next, c in roads[now]:
        dist = c*2+d
        if fox[next] > dist:
            fox[next] = dist
            heappush(HQ, (dist, next))

wolf = [[maxv]*N for _ in range(2)]
HQ = [(0, 0, 1)]
temp = [1, 4]
while HQ:
    d, now, cnt = heappop(HQ)
    if wolf[cnt][now] < d: continue

    cnt = (cnt+1)%2
    for next, c in roads[now]:
        dist = c*temp[cnt]+d
        if wolf[cnt][next] > dist:
            wolf[cnt][next] = dist
            heappush(HQ, (dist, next, cnt))

print(sum([1 if fox[i] < min(wolf[0][i], wolf[1][i]) else 0 for i in range(1, N)]))
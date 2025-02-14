import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lines = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    lines[A].append([B, C])
    lines[B].append([A, C])

costs = [[-1, -1] for _ in range(N+1)]
costs[1] = [0, 0]

from heapq import heappush, heappop
HQ = [[0, 1]]

while HQ:
    v, now = heappop(HQ)
    if v > costs[now][0]: continue

    for next, c in lines[now]:
        if costs[next][0] == -1 or costs[next][0] > v+c:
            costs[next] = [v+c, now]
            heappush(HQ, [v+c, next])

connected = []
for i in range(2, N+1):
    connected.append([i, costs[i][1]])

print(N-1)
for couple in connected:
    print(*couple)
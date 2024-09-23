import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
M = int(input())
infnum = 100000*N+1
cost = [[infnum]*N for _ in range(N)]

for i in range(N):
    cost[i][i] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    cost[a-1][b-1] = min(c, cost[a-1][b-1])

for i in range(N):
    line = cost[i]

    HQ = []
    for j in range(N):
        if i == j or cost[i][j] == infnum: continue
        heappush(HQ, [cost[i][j], j])

    while HQ:
        c, now = heappop(HQ)
        if line[now] < c: continue
        
        for j in range(N):
            if j == i or j == now or cost[now][j] == infnum: continue
            if line[j] == infnum or line[j] > c + cost[now][j]:
                line[j] = c + cost[now][j]
                heappush(HQ, [line[j], j])
    
    for j in range(N):
        print(line[j] if line[j] != infnum else 0, end = ' ')
    print()
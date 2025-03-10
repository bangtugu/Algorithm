import sys
input = sys.stdin.readline

N, M = map(int, input().split())
roads = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, t = map(int, input().split())
    roads[a].append([b, t])
    roads[b].append([a, t])

from heapq import heappush, heappop

min_v = 0
min_lst = []
temp = [-1]*(N+1)
temp[1] = 0
HQ = [[0, 1, '1']]
while HQ:
    v, now, string = heappop(HQ)
    if now == N:
        if temp[N] != -1 and v > temp[N]: continue
        min_v = v
        min_lst = list(map(int, string.split()))

    for next, c in roads[now]:
        if temp[next] == -1 or temp[next] > c + v:
            temp[next] = c+v
            heappush(HQ, [c+v, next, string+' '+str(next)])

answer = 0
for i in range(len(min_lst)-1):
    temp = [-1]*(N+1)
    temp[1] = 0
    HQ = [[0, 1]]

    while HQ:
        v, now = heappop(HQ)

        for next, c in roads[now]:
            if now == min_lst[i] and next == min_lst[i+1]: continue
            if temp[next] == -1 or temp[next] > c + v:
                temp[next] = c+v
                heappush(HQ, [c+v, next])
    
    if temp[N] == -1:
        answer = -1
        break
    else:
        answer = max(answer, temp[N] - min_v)

print(answer)
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
roads = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    roads[A].append(B)

check = [-1]*(N+1)
check[X] = 0

from heapq import heappush, heappop
HQ = []
heappush(HQ, [0, X])

while HQ:
    v, now = heappop(HQ)
    if v == K: continue
    for next in roads[now]:
        if check[next] == -1 or check[next] > v + 1:
            check[next] = v + 1
            heappush(HQ, [v + 1, next])

answer = 0
for i in range(1, N+1):
    if check[i] == K:
        print(i)
        answer += 1

if not answer: print(-1)
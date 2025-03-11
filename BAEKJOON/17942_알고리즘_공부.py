import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
relation = [[] for _ in range(N)]
check = [0]*N
R = int(input())
for _ in range(R):
    a, b, d = map(int, input().split())
    relation[a-1].append([b-1, d])

from heapq import heappop, heappush
HQ = []
for i in range(N):
    heappush(HQ, [lst[i], i])
time = 0
learned = 0
while learned < M and HQ:
    time = HQ[0][0]
    while HQ and HQ[0][0] <= time:
        temp, t = heappop(HQ)
        if check[t]: continue
        check[t] = 1
        learned += 1
        for b, d in relation[t]:
            if not lst[b] or check[b]: continue
            lst[b] = max(lst[b]-d, 0)
            heappush(HQ, [lst[b], b])

print(time)
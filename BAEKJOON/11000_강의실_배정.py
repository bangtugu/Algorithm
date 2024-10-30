import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
lst = []
for _ in range(N):
    a, b = map(int, input().split())
    lst.append([b, a])

lst.sort(key = lambda x: [x[1], x[0]])

answer = 1
HQ = [lst[0][0]]
for i in range(1, N):
    e, s = lst[i]
    while HQ and s >= HQ[0]:
        heappop(HQ)
    heappush(HQ, e)
    answer = max(answer, len(HQ))

print(answer)
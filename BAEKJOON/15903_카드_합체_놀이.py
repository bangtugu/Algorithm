import sys
input = sys.stdin.readline

N, M = map(int, input().split())
HQ = list(map(int, input().split()))

from heapq import heappush, heappop, heapify
heapify(HQ)

for _ in range(M):
    a = heappop(HQ)
    b = heappop(HQ)
    heappush(HQ, a+b)
    heappush(HQ, a+b)

print(sum(HQ))
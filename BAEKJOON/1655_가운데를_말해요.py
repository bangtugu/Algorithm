import sys
input = sys.stdin.readline
import heapq

N = int(input())

LQ = []
RQ = []

for i in range(N):
    new = int(input())

    if len(LQ) == len(RQ):
        heapq.heappush(LQ, -new)
    else:
        heapq.heappush(RQ, new)
        
    if RQ and -LQ[0] > RQ[0]:
        left = heapq.heappop(LQ)
        right = heapq.heappop(RQ)
        heapq.heappush(RQ, -left)
        heapq.heappush(LQ, -right)

    print(-LQ[0])
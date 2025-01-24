import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key = lambda x: [x[0], x[1]])

HQ = []
answer = 0
for s, e in lst:
    while HQ and HQ[0] <= s:
        heappop(HQ)
    heappush(HQ, e)
    answer = max(answer, len(HQ))

print(answer)
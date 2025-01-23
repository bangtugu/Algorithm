import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort(key = lambda x: [x[1], -x[0]])
check = set()

from heapq import heappush, heappop
HQ = []
cnt = 1
for p, d in lst:
    if d < cnt:
        if HQ[0] < p:
            heappop(HQ)
            heappush(HQ, p)
    else:
        heappush(HQ, p)
        cnt += 1

print(sum(HQ))
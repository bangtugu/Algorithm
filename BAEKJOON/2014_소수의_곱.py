import sys
input = sys.stdin.readline
from heapq import heappush, heappop

K, N = map(int, input().split())
entity = list(map(int, input().split()))

HQ = []
for e in entity:
    heappush(HQ, e)

cnt = N
while cnt:
    now = heappop(HQ)
    for e in entity:    
        heappush(HQ, e*now)
        if not now % e: break
    cnt -= 1

print(now)
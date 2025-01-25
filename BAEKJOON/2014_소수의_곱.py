import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N, K = map(int, input().split())
entity = list(map(int, input().split()))

check = set(entity)
HQ = entity[:]
answer = []

while len(answer) < K:
    now = heappop(HQ)
    answer.append(now)
    for e in entity:
        if e*now not in check:
            check.add(e*now)
            heappush(HQ, e*now)

print(answer[-1])
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
HQ = []
maxd = 0
for _ in range(N):
    d, w = map(int, input().split())
    maxd = max(maxd, d)
    heappush(HQ, [-w, d])

check = [i for i in range(maxd+1)]
answer = [0]*(maxd+1)


def get_day(n):
    if check[n] != n:
        check[n] = get_day(check[n])
    return check[n]


while HQ:
    w, d = heappop(HQ)
    day = get_day(d)
    if day:
        answer[day] = -w
        check[day] -= 1

print(sum(answer))
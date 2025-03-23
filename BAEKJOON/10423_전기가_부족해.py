import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())
p_lst = list(map(int, input().split()))
cables = [list(map(int, input().split())) for _ in range(M)]
cables.sort(key = lambda x: x[2])

p = [i for i in range(N+1)]
for i in p_lst:
    p[i] = 0
answer = 0


def get_p(n):
    if p[n] != n:
        p[n] = get_p(p[n])
    return p[n]


def union_p(a, b):
    pa = get_p(a)
    pb = get_p(b)
    if pb < pa: pb, pa = pa, pb
    p[pb] = p[pa]


for a, b, c in cables:
    pa = get_p(a)
    pb = get_p(b)
    if pa == pb: continue
    union_p(a, b)
    answer += c

print(answer)
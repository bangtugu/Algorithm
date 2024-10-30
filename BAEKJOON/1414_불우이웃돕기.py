import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())

lines = [list(input().split()[0]) for _ in range(N)]
total = 0

HQ = []

for i in range(N):
    for j in range(N):
        if lines[i][j] == '0':
            lines[i][j] = 0
        elif ord(lines[i][j])>= 97:
            lines[i][j] = ord(lines[i][j]) - 96
        else:
            lines[i][j] = ord(lines[i][j]) - 38
        total += lines[i][j]
        if lines[i][j]:
            heappush(HQ, [lines[i][j], i, j])

g = list(range(N))


def leader(member):
    if g[member] != member:
        g[member] = leader(g[member])
    return g[member]


while HQ:
    v, i, j = heappop(HQ)
    A, B = leader(i), leader(j)
    if A != B:
        if B < A:
            A, B = B, A
        g[B] = A
        total -= v

for i in range(N):
    if leader(i) != 0:
        print(-1)
        break
else:
    print(total)
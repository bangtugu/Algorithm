import sys
sys.stdin = open('11725_input.txt', 'r')
from collections import deque

N = int(input())
table = [[] for _ in range(N+1)]
p = [0] * (N+1)

for i in range(N-1):
    n1, n2 = map(int, input().split())
    table[n1].append(n2)
    table[n2].append(n1)

Q = deque()
Q.append(1)
p[0] = p[1] = 1

while Q:
    now = Q.popleft()
    for i in table[now]:
        if not p[i]:
            p[i] = now
            Q.append(i)

for num in p[2:]:
    print(num)
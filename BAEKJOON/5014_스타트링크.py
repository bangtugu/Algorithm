import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

check = [-1]*(F+1)
check[S] = 0
from collections import deque
Q = deque([S])

while Q:
    now = Q.popleft()

    for d in [U, -D]:
        if now+d <= 0 or now+d > F or check[now+d] != -1: continue
        check[now+d] = check[now]+1
        Q.append(now+d)

if check[G] == -1:
    check[G] = 'use the stairs'

print(check[G])
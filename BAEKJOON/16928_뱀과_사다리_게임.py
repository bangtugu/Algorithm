import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
lands = {}
for _ in range(N+M):
    a, b = map(int, input().split())
    lands[a] = b

check = [0]*101

Q = deque([[1, 0]])
while Q:
    if check[-1]: break

    now, cnt = Q.popleft()
    for i in range(1, 7):
        if now+i > 100: break
        if check[now+i]: continue
        check[now+i] = cnt + 1
        if now+i in lands:
            check[lands[now+i]] = cnt + 1
            Q.append([lands[now+i], cnt+1])
        else:
            Q.append([now+i, cnt+1])

print(check[-1])
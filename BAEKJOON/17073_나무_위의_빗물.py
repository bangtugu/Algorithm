import sys
input = sys.stdin.readline

N, W = map(int, input().split())
nodes = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

check = [0]*(N+1)
check[1] = 1
from collections import deque
Q = deque([1])
cnt = 0

while Q:
    now = Q.popleft()

    temp = 0
    for next in nodes[now]:
        if check[next]: continue
        temp += 1
        check[next] = 1
        Q.append(next)
    
    if not temp:
        cnt += 1

print(W/cnt)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
check = [-1]*(N+1)
node = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())

    node[a].append(b)
    node[b].append(a)

from collections import deque
check[1] = 0
Q = deque([1])

while Q:
    now = Q.popleft()

    for next in node[now]:
        if check[next] != -1: continue
        check[next] = check[now]+1
        Q.append(next)

answer = [-1, -1, -1]
for i in range(1, N+1):
    if check[i] > answer[1]:
        answer = [i, check[i], 1]
    elif check[i] == answer[1]:
        answer[2] += 1

print(*answer)
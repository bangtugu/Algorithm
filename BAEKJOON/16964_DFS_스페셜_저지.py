import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
node = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

p = [0]*(N+1)
child = [[] for _ in range(N+1)]

Q = deque()
Q.append(1)
p[1] = 1
while Q:
    now = Q.popleft()
    for c in node[now]:
        if p[c]: continue
        p[c] = now
        child[now].append(c)
        Q.append(c)

answer = 1
result = list(map(int, input().split()))
can_move = [set([1])]
for i in range(N):
    if result[i] not in can_move[-1]:
        answer = 0
        break
    
    can_move[-1].remove(result[i])
    if not can_move[-1]: can_move.pop()
    if child[result[i]]: can_move.append(set(child[result[i]]))
    
print(answer)
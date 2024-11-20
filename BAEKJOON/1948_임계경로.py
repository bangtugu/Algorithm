import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())
road = [[] for _ in range(N+1)]
coming = [0]*(N+1)
for _ in range(M):
    a, b, c = map(int, input().split())
    road[a].append([b, c])
    coming[b] += 1

s, e = map(int, input().split())

cnt = [[] for _ in range(N+1)]
dist = [0]*(N+1)
Q = deque([s])
while Q:
    now = Q.popleft()
    if now == e: continue

    for b, c in road[now]:
        coming[b] -= 1

        if dist[b] < dist[now] + c:
            dist[b] = dist[now] + c
            cnt[b] = [now]
        elif dist[b] == dist[now] + c:
            cnt[b].append(now)
        
        if not coming[b]:
            Q.append(b)

temp = set()
Q = deque([e])
while Q:
    now = Q.popleft()

    for n in cnt[now]:
        if (n, now) not in temp:
            temp.add((n, now))
            Q.append(n)

print(dist[e])
print(len(temp))
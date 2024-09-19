import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
check = [-1]*100001
check[N] = 0
Q = deque([[N, 0]])
while Q:
    now, now_time = Q.popleft()
    if check[now] > now_time: continue
    if check[K] != -1 and check[K] <= now_time: continue

    for next, cost in [[now * 2, 0], [now - 1, 1], [now + 1, 1]]:
        if next < 0 or next > 100000: continue
        if check[next] == -1 or now_time+cost < check[next]:
            check[next] = now_time+cost
            Q.append([next, check[next]])

print(check[K])
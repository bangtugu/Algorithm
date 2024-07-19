import sys
input = sys.stdin.readline

N, K = map(int, input().split())
check = [0]*100001

from collections import deque
Q = deque()
Q.append(N)
check[N] = 1

answer = 0
while Q:
    now = Q.popleft()
    
    if now == K:
        answer += 1
        continue
    
    if answer:
        continue
    
    for n in [now+1, now-1, now*2]:
        if not 0 <= n <= 100000: continue
        if not check[n]:
            check[n] = check[now]+1
            Q.append(n)
        elif check[now] == check[n]-1:
            Q.append(n)

print(check[K]-1)
print(answer)
from collections import deque

N = int(input())

lst = list(map(int, input().split()))

v = [N]*N
v[0] = 0

now = 0

while now < N:
    for i in range(lst[now]):
        if now + i + 1 < N:
            v[now+1+i] = min(v[now+1+i], v[now]+1)
        else:
            break

if v[-1] == N:
    print(-1)
else:
    print(v[-1])
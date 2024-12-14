import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]

s, e = 0, max(lst)
answer = -1
while s <= e:

    m = (s+e)//2
    if not m:
        break
    cnt = 0
    for i in range(N):
        cnt += lst[i]//m

    if cnt >= K:
        answer = m
        s = m + 1
    else:
        e = m - 1

print(answer)
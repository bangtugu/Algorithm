import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

s = 0
e = max(trees)
while s <= e:
    temp = 0
    m = (s + e)//2

    for n in trees:
        now = n - m
        if now <= 0: continue
        temp += now

    if temp < M:
        e = m - 1
    elif temp > M:
        s = m + 1
    else:
        e = m
        break

print(e)
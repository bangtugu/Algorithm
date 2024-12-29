import sys
input = sys.stdin.readline

N, M = map(int, input().split())
costs = [int(input()) for _ in range(N)]

s = max(costs)
e = sum(costs)


def check(n):
    cnt = 1
    temp = n

    for cost in costs:
        if cost <= temp:
            temp -= cost
        else:
            cnt += 1
            temp = n - cost
    
    if cnt <= M:
        return True
    else:
        return False

while s < e:
    m = (s+e)//2

    if check(m):
        e = m
    else:
        s = m + 1

print(s)
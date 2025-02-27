import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
T = 1


def check(n):
    temp = [1]*M
    for i in range(M):
        temp[i] += n//lst[i]
    return temp


while sum(check(T)) < N:
    T *= 2

s, e = T//2, T
while s < e:
    m = (s+e)//2
    temp = check(m)
    if sum(check(m)) >= N:
        T = m
        e = m
    else:
        s = m + 1

temp = check(T)
if sum(temp) >= N:
    for i in range(M):
        temp[i] -= 1

cnt = N-sum(temp)
for i in range(M):
    temp[i] = temp[i]*lst[i]

answer = 0
while cnt:
    minv = min(temp)
    for i in range(M):
        if temp[i] == minv:
            temp[i] += lst[i]
            cnt -= 1
            answer = i+1
            if not cnt: break

print(answer)
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
lst = list(map(int, input().split()))
s, e = 0, 0

answer = 0
now = lst[0]
while True:

    if now >= S:
        if not answer: answer = e-s+1
        answer = min(answer, e-s+1)
    
    if now < S or s == e:
        e += 1
        if e == N: break
        now += lst[e]
    else:
        now -= lst[s]
        s += 1

print(answer)
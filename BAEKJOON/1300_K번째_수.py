import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

s, e = 1, K+1
answer = 0

while s < e:
    m = (s+e)//2
    temp = 0
    
    for i in range(1, N+1):
        temp += min(m//i, N)
    
    if temp < K:
        s = m + 1
    else:
        answer = m
        e = m

print(answer)
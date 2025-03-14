import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
from math import gcd

left = [0]*(N+1)
right = [0]*(N+1)
left[0] = lst[0]
right[N-1] = lst[N-1]

for i in range(1, N):
    left[i] = gcd(left[i-1], lst[i])
for i in range(N-2, -1, -1):
    right[i] = gcd(right[i+1], lst[i])

answer = [-1]
for i in range(N):
    if not i:
        temp = right[1]
    elif i == N-1:
        temp = left[N-1]
    else:
        temp = gcd(left[i-1], right[i+1])

    if lst[i]%temp:
        if temp > answer[0]:
            answer = [temp, lst[i]]

print(*answer)
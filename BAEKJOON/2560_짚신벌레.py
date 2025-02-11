import sys
input = sys.stdin.readline
from collections import deque

a, b, d, N = map(int, input().split())

Q = deque([1]+[0]*(d-1))
temp = 0

for day in range(N):

    temp += Q[a-1]
    temp -= Q[b-1]
    temp %= 1000
    Q.appendleft(temp)
    Q.pop()

print(sum(Q)%1000)
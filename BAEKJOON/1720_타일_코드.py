import sys
input = sys.stdin.readline

N = int(input())
lst = [0] * (N+1)
lst[0], lst[1] = 1, 1
for i in range(2, N+1):
    lst[i] = lst[i-2]*2 + lst[i-1]

if N%2:
    temp = lst[N//2]
else:
    temp = lst[N//2] + lst[N//2-1]*2
print((lst[N]-temp)//2 + temp)
import sys
input = sys.stdin.readline

mod = 1000000007
N = int(input())
lst = list(map(int, input().split()))
lst.sort()
temp = [1]*N
for i in range(1, N):
    temp[i] = (temp[i-1]*2)%mod
answer = 0
for i in range(N):
    now = lst[i]

    answer += now*temp[i] + (-now)*temp[N-1-i]
    answer %= mod

print(answer%mod)
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
S = int(input())

for i in range(N-1):
    if not S: break

    maxv, idx = 0, 0
    for j in range(S+1):
        if i+j >= N: break
        if lst[i+j] > maxv:
            maxv = lst[i+j]
            idx = j
    S -= idx
    for j in range(idx-1, -1, -1):
        lst[i+j+1] = lst[i+j]
    lst[i] = maxv

print(*lst)
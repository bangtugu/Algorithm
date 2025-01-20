import sys
input = sys.stdin.readline
from itertools import combinations

N, L, R, X = map(int, input().split())
lst = sorted(list(map(int, input().split())))


def check(l, r):    
    cnt = 0
    for i in range(1, r-l):
        for case in combinations(lst[l+1:r], i):
            if L <= sum(case)+lst[r]+lst[l] <= R:
                cnt += 1
    
    return cnt


l, r = 0, 0
answer = 0
while l < N:

    if lst[r] - lst[l] >= X:
        if L <= lst[r]+lst[l] <= R: answer += 1
        answer += check(l, r)
    
    r += 1
    if r >= N:
        l += 1
        r = l

print(answer)
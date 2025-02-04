import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

if max(lst) > 1440 or sum(lst) > 2880:
    print(-1)
else:
    if max(lst) >= sum(lst)-max(lst):
        print(max(lst))
    else:
        print(sum(lst)//2 + sum(lst)%2)
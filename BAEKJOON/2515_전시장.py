import sys
input = sys.stdin.readline

N, S = map(int, input().split())
dic = {}
for _ in range(N):
    H, C = map(int, input().split())
    if H in dic:
        dic[H] = max(dic[H], C)
    else:
        dic[H] = C

lst = sorted(list(dic.keys()))

N = len(lst)
for i in range(1, N):
    H, C = lst[i], dic[lst[i]]
    s = 0
    e = N
    cost = 0
    while s <= e:
        m = (s + e)//2
        if lst[m] <= H-S:
            cost = dic[lst[m]]
            s = m + 1
        else:
            e = m - 1

    dic[lst[i]] = max(dic[lst[i-1]], C+cost)

print(dic[lst[-1]])
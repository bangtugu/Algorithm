import sys
input = sys.stdin.readline

V = int(input())
dic_lst = [{} for _ in range(V+1)]
for _ in range(V):
    temp = list(map(int, input().split()))
    now = temp[0]

    i = 1
    while temp[i] != -1:
        if temp[i] not in dic_lst[now]:
            dic_lst[now][temp[i]] = temp[i+1]
            dic_lst[temp[i]][now] = temp[i+1]
        i += 2

from heapq import heappush, heappop
check1 = [-1]*(V+1)
check2 = [-1]*(V+1)


def find_max_idx(s, lst):
    max_idx = s
    max_value = 0

    HQ = [[0, s]]
    while HQ:
        value, now = heappop(HQ)
        if lst[now] < value: continue
        if value > max_value:
            max_idx, max_value = now, value

        for i in dic_lst[now]:
            if lst[i] == -1 or lst[i] > value + dic_lst[now][i]:
                lst[i] = value + dic_lst[now][i]
                heappush(HQ, [lst[i], i])

    return max_idx


check1[1] = 0
first_max = find_max_idx(1, check1)
check2[first_max] = 0
print(check2[find_max_idx(first_max, check2)])
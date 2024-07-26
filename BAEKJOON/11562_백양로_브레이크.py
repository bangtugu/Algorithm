import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [[i] for i in range(N)]
cost = [[N**2]*N for _ in range(N)]

possible_path = {}
for _ in range(M):
    a, b, c = map(int, input().split())
    if c:
        cost[b-1][a-1] = 0
        lst[b-1].append(a-1)
    else:
        if b-1 not in possible_path:
            possible_path[b-1] = []
        possible_path[b-1].append(a-1)
    cost[a-1][b-1] = 0
    lst[a-1].append(b-1)

cost_lst = [[] for _ in range(N)]
for i in range(N):
    temp = lst[i][:]
    check = set(temp)
    cnt = 0
    while cnt < len(cost_lst[i])+1:
        idx = 0
        while idx < len(temp):
            now = temp[idx]
            cost[i][now] = min(cost[i][now], cnt)
            for n in lst[now]:
                if n == i or n in check: continue
                check.add(n)
                temp.append(n)
            idx += 1

        if temp: cost_lst[i].append(temp)
        temp = []
        for n in cost_lst[i][-1]:
            if n not in possible_path: continue
            for n2 in possible_path[n]:
                if n2 == i or n2 in check: continue
                temp.append(n2)
                check.add(n2)
        cnt += 1

K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    print(cost[a-1][b-1])
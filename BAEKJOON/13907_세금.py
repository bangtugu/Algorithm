import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N, M, K = map(int, input().split())
S, D = map(int, input().split())
roads = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    roads[a].append([b, c])
    roads[b].append([a, c])

HQ = [[0, S, 0]]
cost = [0] * (N+1)
max_cnt = 0

while HQ:
    c1, now, cnt = heappop(HQ)
    if cost[now] and cost[now] < c1: continue
    if now == D:
        max_cnt = cnt
        break
    for next, c2 in roads[now]:
        if next == S: continue
        if not cost[next] or cost[next] > c1 + c2:
            cost[next] = c1 + c2
            heappush(HQ, [cost[next], next, cnt+1])


cost_lst = [[-1]*(max_cnt+1) for _ in range(N+1)]
for i in range(max_cnt+1):
    cost_lst[S][i] = 0
cost_lst[D][max_cnt] = cost[D]
HQ = [[0, S, 0]]
cnt_lst = [max_cnt]

while HQ:
    c1, now, cnt = heappop(HQ)
    if cnt >= max_cnt: continue
    if cost_lst[now][cnt] != -1 and cost_lst[now][cnt] < c1: continue
    if now == D:
        cnt_lst.append(cnt)
        continue
    for next, c2 in roads[now]:
        if cost_lst[next][cnt+1] == -1 or cost_lst[next][cnt+1] > c1 + c2:
            cost_lst[next][cnt+1] = c1 + c2
            heappush(HQ, [c1 + c2, next, cnt+1])

cost_lst = cost_lst[D]
cnt_lst.sort(reverse = True)
tax = 0
idx = 0
print(cost_lst[cnt_lst[0]])
for _ in range(K):
    tax += int(input())
    min_v = cost_lst[cnt_lst[0]] + tax*cnt_lst[0]
    min_idx = 0
    for i in range(len(cnt_lst)):
        now_v = cost_lst[cnt_lst[i]] + tax*cnt_lst[i]
        if now_v <= min_v:
            min_v = now_v
            min_idx = i
    print(min_v)
    cnt_lst = cnt_lst[min_idx:]


'''
6 6 4
1 6
1 2 3
2 3 2
3 4 1
1 4 9
4 5 1
5 6 1
1
1
1
1

8
13
17
20
23
'''

'''
4 4 2
1 4
1 2 1
2 3 1
3 4 1
1 3 3
1
1

3
6
8

'''
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

cost_lst = [[-1]*(N+1) for _ in range(N+1)]
HQ = [[0, S, 0]]
cnt_lst = []

while HQ:
    c1, now, cnt = heappop(HQ)
    if cost_lst[now][cnt] != -1 and cost_lst[now][cnt] < c1: continue
    if now == D:
        cnt_lst.append(cnt)
        continue
    for next, c2 in roads[now]:
        if next == S: continue
        if cost_lst[next][cnt+1] == -1 or cost_lst[next][cnt+1] > c1 + c2:
            cost_lst[next][cnt+1] = c1 + c2
            heappush(HQ, [c1 + c2, next, cnt+1])

cnt_lst.sort(reverse = True)
tax = 0
idx = 0
print(cnt_lst)
for _ in range(K):
    tax += int(input())
    while idx+1 < len(cnt_lst) and cost_lst[D][cnt_lst[idx]] + tax*cnt_lst[idx] >= cost_lst[D][cnt_lst[idx+1]] + tax*cnt_lst[idx+1]:
        idx += 1
    print(cost_lst[D][cnt_lst[idx]] + tax*cnt_lst[idx])



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
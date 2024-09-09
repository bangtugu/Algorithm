import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())

lst = [{} for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    if b in lst[a]:
        lst[a][b] = max(lst[a][b], c)
        lst[b][a] = max(lst[b][a], c)
    else:
        lst[a][b] = c
        lst[b][a] = c

key_lst = [sorted(lst[i].keys(), key = lambda x: -lst[i][x]) for i in range(N+1)]

A, B = map(int, input().split())
max_v = 1000000001
can_trans = [max_v]*(N+1)
HQ = []
for i in key_lst[A]:
    can_trans[i] = lst[A][i]
    heapq.heappush(HQ, [-lst[A][i], i])

while HQ:
    g, now = heapq.heappop(HQ)
    if can_trans[B] != max_v and -g < can_trans[B]: continue
    
    for i in key_lst[now]:
        if i == A: continue
        if can_trans[i] == max_v or can_trans[i] < min(lst[now][i], -g):
            can_trans[i] = min(lst[now][i], -g)
            heapq.heappush(HQ, [-min(lst[now][i], -g), i])   

print(can_trans[B])
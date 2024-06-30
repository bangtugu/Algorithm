import sys
input = sys.stdin.readline
# sys.setrecursionlimit(1000) # 재귀시 사용

di = [-4, -5, -1, 3, 4, 5, 1, -3]
pool = [[0, 0] for _ in range(16)]
spot = [-1]*17
d_lst = [-1]*16

for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        n, d = line[j*2], line[j*2+1]-1
        pool[i*4+j] = n
        d_lst[n] = d
        spot[n] = i*4+j

answer = pool[0]
spot[pool[0]] = -1
pool[0] = 0

from collections import deque
Q = deque()
Q.append([0, answer, pool, spot, d_lst])
answer = 0

while Q:
    value, pool, spot, d_lst = Q.popleft()
    #물고기이동
    for fish in range(1, 17):
        if spot[fish] == -1: continue
        idx = spot[fish]
        d = d_lst[idx]
        cnt = 0
        while idx+di[d] < 0 or idx+di[d] >= 16 or pool[idx+di[d]] == 0:
            d = (d+1)%8
            cnt += 1
            if cnt >= 8: break
        if cnt >= 8: continue
        d_lst[idx] = d
        target_idx = idx+di[d]
        target_fish = pool[target_idx]
        spot[fish], spot[target_fish] = spot[target_fish], spot[fish]
        pool[idx], pool[target_idx] = pool[target_idx], pool[idx]
        d_lst[idx], d_lst[target_idx] = d_lst[target_idx], d_lst[idx]

    #상어이동
    shark = 0
    idx = spot[0]
    d = d_lst[idx]
    target_idx = idx+di[d]
    while 0 <= target_idx < 16:
        if 0 < pool[idx+di[d]] < 17:
            target_fish = pool[target_idx]
            spot[0] = spot[target_fish]
            spot[target_fish] = -1
            pool[spot[0]] = 0
            Q.append(value+target_fish, pool, spot, d_lst)
            pool[spot[0]] = 1
            j = j+di[d]
        
        target_fish += di[d]
print(answer)
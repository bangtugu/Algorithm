import sys
input = sys.stdin.readline
# sys.setrecursionlimit(1000) # 재귀시 사용

N = int(input())

complete = [0]*N
need_time = [0]*N
need_lst = {}

for i in range(N):
    temp = list(map(int, input().split()))
    need_time[i] = temp[0]
    need_lst[i] = temp[1:-1]

while True:
    change = 0

    for i in range(N):
        if complete[i]: continue

        if not need_lst[i]:
            complete[i] = need_time[i]
            continue

        lst = [complete[need-1] for need in need_lst[i]]
        if min(lst) == 0: continue
        
        change += 1
        complete[i] = max(lst) + need_time[i]

    if not change: break

for t in complete:
    print(t)
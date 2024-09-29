import sys
input = sys.stdin.readline

N, M = map(int, input().split())

each_depth = [0]*(N+1)
need_right = [[] for _ in range(N+1)]
need_cnt = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    need_right[a].append(b)
    need_cnt[b] += 1

temp = []
for i in range(1, N+1):
    if not need_cnt[i]:
        temp.append(i)

answer = []
while temp:
    next_temp = []

    for now in temp:
        answer.append(now)
        for n in need_right[now]:
            need_cnt[n] -= 1
            if not need_cnt[n]: next_temp.append(n)
    
    temp = next_temp

print(*answer)
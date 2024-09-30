import sys
input = sys.stdin.readline

N, M = map(int, input().split())

need_left = [set() for _ in range(N+1)]
need_right = [[] for _ in range(N+1)]
need_cnt = [0]*(N+1)

for _ in range(M):
    line = list(map(int, input().split()))
    now = line[0]
    for i in range(1, now):
        if line[i] in need_left[line[i+1]]: continue
        need_right[line[i]].append(line[i+1])
        need_cnt[line[i+1]] += 1

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

if len(answer) == N:
    for n in answer:
        print(n)
else:
    print(0)
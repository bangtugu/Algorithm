import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

parent = list(range(N))
connected = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    if parent[i] != i: continue

    sett = set([i])
    lst = [i]
    idx = 0
    while idx < len(lst):
        now = lst[idx]

        for j in range(N):
            if j in sett: continue
            if connected[now][j]:
                parent[j] = i
                lst.append(j)
                sett.add(j)

        idx += 1

city = list(map(int, input().split()))
group = parent[city[0]-1]
for i in range(1, M):
    if group != parent[city[i]-1]:
        print('NO')
        break
else:
    print('YES')
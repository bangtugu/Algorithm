import sys
input = sys.stdin.readline
from collections import deque

TC = int(input())

for tc in range(TC):
    N, M, W = map(int, input().split())

    table = [[False]*N for _ in range(N)]
    path = [set() for _ in range(N)]

    for _ in range(M):
        s, e, d = map(int, input().split())
        if s == e: continue
        table[s-1][e-1] = d if table[s-1][e-1] == False else min(d, table[s-1][e-1])
        table[e-1][s-1] = d if table[e-1][s-1] == False else min(d, table[e-1][s-1])
        path[s-1].add(e-1)
        path[e-1].add(s-1)

    ws = set()
    for _ in range(W):
        s, e, d = map(int, input().split())
        table[s-1][e-1] = -d if table[s-1][e-1] == False else min(-d, table[s-1][e-1])
        ws.add((s-1, e-1))
        path[s-1].add(e-1)

    for i in range(N):
        if not table[i][i]: table[i][i] = 0
        path[i] = list(path[i])


    Q = deque()
    for s, e in ws:
        Q.append([s, e, table[s][e]])
    loop = False

    while Q:
        s, now, v = Q.popleft()
        if loop: break

        if table[s][now] < v: continue

        for e in path[now]:
            if table[s][e] is False:
                table[s][e] = table[s][now] + table[now][e]
                Q.append([s, e, table[s][e]])
            elif table[s][e] > table[s][now] + table[now][e]:
                table[s][e] = table[s][now] + table[now][e]
                Q.append([s, e, table[s][e]])
            if e == s and table[s][s] < 0:
                loop = True

    if loop:
        print('YES')
    else:
        print('NO')
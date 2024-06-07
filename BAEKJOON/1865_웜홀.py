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
        table[s-1][e-1] = d if not table[s-1][e-1] else min(d, table[s-1][e-1])
        table[e-1][s-1] = d if not table[e-1][s-1] else min(d, table[e-1][s-1])
        path[s-1].add(e-1)
        path[e-1].add(s-1)

    ws = []
    for _ in range(W):
        s, e, d = map(int, input().split())
        table[s-1][e-1] = -d if not table[s-1][e-1] else min(-d, table[s-1][e-1])
        ws.append(s-1)
        path[s-1].add(e-1)

    for i in range(N):
        table[i][i] = 0
        path[i] = list(path[i])

    loop = False
    for s in ws:
        if loop: break
        Q = deque()
        for e in path[s]:
            Q.append(e)
        while Q:
            if table[s][s] < 0:
                loop = True
                break
            now = Q.popleft()
            for e in path[now]:
                if table[s][e] == False:
                    table[s][e] = table[s][now] + table[now][e]
                    Q.append(e)
                elif table[s][now] + table[now][e] < table[s][e]:
                    table[s][e] = table[s][now] + table[now][e]
                    Q.append(e)

    if loop:
        print('YES')
    else:
        print('NO')
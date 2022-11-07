from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(lst, n):

    now_empty = empty

    temp = [[-1]*N for _ in range(N)]
    Q = deque()
    for vi in lst:
        temp[vi[0]][vi[1]] = 0
        Q.append(vi)

    maxnum = 0

    while Q:

        y, x = Q.popleft()

        for i in range(4):

            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N and lab[ny][nx] != 1 and temp[ny][nx] == -1:
                temp[ny][nx] = temp[y][x] + 1
                if temp[y][x] >= n:
                    return n
                maxnum = max(maxnum, temp[ny][nx])
                if lab[ny][nx] != 2:
                    now_empty -= 1
                    if not now_empty:
                        return maxnum
                Q.append([ny, nx])

    if now_empty:
        return 0

    return maxnum


N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

virus = []
empty = 0

for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append([i, j])
        elif lab[i][j] == 0:
            empty += 1

if empty:

    ans = N*N

    for vir in combinations(virus, M):
        new_ans = bfs(vir, ans)
        if new_ans:
            ans = min(ans, new_ans)

    if ans == N*N:
        print(-1)
    else:
        print(ans)
else:
    print(0)
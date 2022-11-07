from collections import deque


def makewall(y, n):
    if n >= 3:
        bfs()
        return

    for i in range(y, N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                makewall(i, j, n+1)
                lab[i][j] = 0


def bfs():

    Q = deque()

    v = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if lab[i][j]:
                v[i][j] = 1
                if lab[i][j] == 2:
                    Q.append((i, j))

    while Q:
        nowy, nowx = Q.popleft()

        for d in range(4):
            newy = nowy + dy[d]
            newx = nowx + dx[d]

            if 0 <= newy < N and 0 <= newx < M and not v[newy][newx]:
                Q.append((newy, newx))
                v[newy][newx] = 1

    safe_zone = 0
    for line in v:
        safe_zone += line.count(0)

    global max_safe_zone
    max_safe_zone = max(safe_zone, max_safe_zone)


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

max_safe_zone = 0

makewall(0, 0, 0)

print(max_safe_zone)
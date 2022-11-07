from collections import deque


def solution(maps):
    N = len(maps)
    M = len(maps[0])

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    Q = deque()
    Q.append((0, 0))

    while Q:
        y, x = Q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                Q.append((ny, nx))

    if maps[N - 1][M - 1] == 1:
        answer = -1
    else:
        answer = maps[N - 1][M - 1]

    return answer
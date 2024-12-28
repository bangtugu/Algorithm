import sys
input = sys.stdin.readline

M, N = map(int, input().split())
field = [input() for _ in range(N)]
check = [[0]*M for _ in range(N)]
answer = [0, 0]

from collections import deque
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
for i in range(N):
    for j in range(M):
        if check[i][j]: continue
        cnt = 1
        check[i][j] = 1
        Q = deque()
        Q.append([i, j])
        while Q:
            y, x = Q.popleft()

            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if ny < 0 or nx < 0 or ny >= N or nx >= M or check[ny][nx] or field[i][j] != field[ny][nx]: continue
                cnt += 1
                check[ny][nx] = 1
                Q.append([ny, nx])
        
        if field[i][j] == 'W':
            answer[0] += cnt**2
        else:
            answer[1] += cnt**2

print(*answer)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [input().split()[0] for _ in range(N)]
temp = {
    'U': 1,
    'R': 2,
    'D': 3,
    'L': 4
}
dy, dx = [0, 1, 0, -1, 0], [0, 0, -1, 0, 1]

check = [[0]*(M+2) for _ in range(N+2)]
for i in range(N):
    for j in range(M):
        check[i+1][j+1] = temp[lst[i][j]]

from collections import deque
answer = 0
Q = deque()
for i in range(N+2):
    Q.append((i, 0))
    Q.append((i, M+1))
for j in range(M):
    Q.append((0, j+1))
    Q.append((N+1, j+1))

while Q:
    y, x = Q.popleft()

    for d in range(1, 5):
        ny = y + dy[d]
        nx = x + dx[d]
        if ny < 0 or nx < 0 or ny >= N+2 or nx >= M+2 or d != check[ny][nx]: continue
        check[ny][nx] = 0
        Q.append((ny, nx))
        answer += 1

print(answer)
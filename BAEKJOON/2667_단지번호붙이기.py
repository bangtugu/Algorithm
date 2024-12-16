import sys
input = sys.stdin.readline

N = int(input())
town = [input() for _ in range(N)]
check = [[0]*N for _ in range(N)]
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

from collections import deque
cnt = 0
answer = []
Q = deque()
for i in range(N):
    for j in range(N):
        if town[i][j] == '1' and not check[i][j]:
            cnt += 1
            temp = 1
            check[i][j] = cnt
            Q.append([i, j])
            while Q:
                y, x = Q.popleft()

                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]

                    if ny < 0 or nx < 0 or ny >= N or nx >= N or check[ny][nx] or town[ny][nx] != '1': continue
                    check[ny][nx] = cnt
                    temp += 1
                    Q.append([ny, nx])
            answer.append(temp)

answer.sort()
print(cnt)
for n in answer:
    print(n)
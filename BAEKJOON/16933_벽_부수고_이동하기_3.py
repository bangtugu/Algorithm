import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())
field = [input() for _ in range(N)]
check = [[-1]*M for _ in range(N)]
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
Q = deque()

Q.append([0, 0, 0, 1])
check[0][0] = 1
answer = -1
cnt = 1
while Q:
    print(Q)
    y, x, c, l = Q.popleft()

    if y == N-1 and x == M-1:
        answer = l
        break
    
    day = l%2
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
        if field[ny][nx] == '0' and check[ny][nx] == -1:
            check[ny][nx] = l + 1
            Q.append([ny, nx, c, l+1])
        
        if field[ny][nx] == '1' and c < K:
            if day:
                if check[ny][nx] == -1:
                    check[ny][nx] = l+1
                    Q.append([ny, nx, c+1, l+1])
            else:
                Q.append([y, x, c, l+1])

print(answer)
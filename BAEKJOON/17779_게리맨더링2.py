import sys
from pprint import pprint
from collections import deque
input = sys.stdin.readline

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def check(y, x, d1, d2):
    temp = [[0]*N for _ in range(N)]
    area = [0, 0, 0, 0, 0]

    for i in range(d1+1):
        temp[y-i][x+i] = 5
        temp[y+d2-i][x+d2+i] = 5
        for j in range(d2+1):
            temp[y+j][x+j] = 5
            temp[y-d1+j][x+d1+j] = 5

    Q = deque()

    Q.append([y, x+1])
    temp[y][x+1] = 5

    while Q:

        ny, nx = Q.popleft()

        for i in range(4):

            nny = dy[i]
            nnx = dx[i]

            if city[nny][nnx] == 0 and temp[nny][nnx] == 0:
                temp[nny][nnx] = 5
                Q.append([nny, nnx])

    pprint(temp)

    for i in range(N):
        for j in range(N):
            if not temp[i][j]:
                if 0 <= i <= x+d1 and 0 <= j < y:
                    temp[i][j] = 1
                elif 0 <= i <= x+d2 and y <= j < N:
                    temp[i][j] = 2
                elif x+d1 < i < N and 0 <= j <= y-d1+d2:
                    temp[i][j] = 3
                elif x+d2 < i < N and y-d1+d2 < j < N:
                    temp[i][j] = 4

    pprint(temp)


    return max(area) - min(area)


N = int(input())

city = [list(map(int, input().split())) for _ in range(N)]

ans = N*N*100

for i in range(1, N-1):
    for j in range(N-2):
        for z in range(1, i+1):
            for w in range(1, N-i):
                if j + z + w < N:
                    pass
                    # ans = min(ans, check(i, j, z, w))
check(1, 0, 1, 3)


print(ans)
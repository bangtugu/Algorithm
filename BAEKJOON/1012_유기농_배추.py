import sys
sys.stdin = open('1012_input.txt', 'r')


# def check(y, x):
#     for i in range(4):
#         yy = y + dy[i]
#         xx = x + dx[i]
#         if 0 <= yy < N and 0 <= xx < M:
#             if farm[yy][xx] == -1:
#                 farm[yy][xx] = cnt
#                 check(yy, xx)
#
#
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     M, N, K = map(int, input().split())
#     farm = [[0] * M for _ in range(N)]
#
#     for i in range(K):
#         x, y = map(int, input().split())
#         farm[y][x] = -1
#
#     cnt = 0
#
#     for i in range(N):
#         for j in range(M):
#             if farm[i][j] == -1:
#                 cnt += 1
#                 farm[i][j] = cnt
#                 check(i, j)
#
#     print('#{} {}'.format(test_case, cnt))

import sys
sys.setrecursionlimit(10**6)


def check(y, x):
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        if 0 <= yy < N and 0 <= xx < M and farm[yy][xx] == -1:
            farm[yy][xx] = cnt
            check(yy, xx)


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

T = int(input())

for test_case in range(1, T+1):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        farm[y][x] = -1

    cnt = 0

    for i in range(N):
        for j in range(M):
            if farm[i][j] == -1:
                cnt += 1
                farm[i][j] = cnt
                check(i, j)

    print(cnt)


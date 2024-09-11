import sys
input = sys.stdin.readline

R, C, Q = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(R)]
sum_lst = [[0]*(C+1) for _ in range(R+1)]

for i in range(1, R+1):
    for j in range(1, C+1):
        sum_lst[i][j] = mapp[i-1][j-1] - sum_lst[i-1][j-1] + sum_lst[i][j-1] + sum_lst[i-1][j]

for _ in range(Q):
    y1, x1, y2, x2 = map(int, input().split())
    cnt = (y2-y1+1)*(x2-x1+1)
    temp = sum_lst[y2][x2] + sum_lst[y1-1][x1-1] - sum_lst[y2][x1-1] - sum_lst[y1-1][x2]
    print(temp//cnt)
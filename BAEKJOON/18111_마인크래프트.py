# import sys
#
# N, M, B = map(int, sys.stdin.readline().split())
#
# ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#
# total = 0
# for line in ground:
#     total += sum(line)
#
# target = total//(N*M)
# over_ground = total%(N*M)
#
# if over_ground * 2 > N*M - over_ground and N*M - over_ground <= B:
#     target += 1
#
# time = 0
#
# for i in range(N):
#     for j in range(M):
#         if ground[i][j] < target:
#             time += (target - ground[i][j])
#         elif ground[i][j] > target:
#             time += (ground[i][j] - target) * 2
#
# print(time, target)
#
# 블럭을 놓는게 파내는거보다 시간이 덜 걸린다는걸 간과한 코드


import sys

N, M, B = map(int, sys.stdin.readline().split())

ground = []

for _ in range(N):
    ground += list(map(int, sys.stdin.readline().split()))

total = sum(ground)

height = total//(N*M)
B += total%(N*M)

min_time = 500*500*512
max_height = 0

while B >= 0:

    now_time = 0

    for i in range(len(ground)):
        if ground[i] < height:
            now_time += (height - ground[i])
        elif ground[i] > height:
            now_time += (ground[i] - height) * 2

    if now_time <= min_time:
        min_time = now_time
        max_height = height

    height += 1
    B -= M*N

## 시간초과

print(min_time, max_height)




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


# import sys
#
# N, M, B = map(int, sys.stdin.readline().split())
#
# ground = []
#
# for _ in range(N):
#     ground += list(map(int, sys.stdin.readline().split()))
#
# total = sum(ground)
#
# height = total//(N*M)
# B += total%(N*M)
#
# min_time = 500*500*512
# max_height = 0
#
# while B >= 0:
#
#     now_time = 0
#
#     for i in range(len(ground)):
#         if ground[i] < height:
#             now_time += (height - ground[i])
#         elif ground[i] > height:
#             now_time += (ground[i] - height) * 2
#
#     if now_time <= min_time:
#         min_time = now_time
#         max_height = height
#
#     height += 1
#     B -= M*N
#
# ## 시간초과
#
# print(min_time, max_height)



# N, M, B = map(int, input().split())
# land = [list(map(int, input().split())) for _ in range(N)]

# result_time = 0

# total = 0

# for line in land:
#     total += sum(line)

# average = total//(N*M)

# print(result_time, land[0][0], total)


import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
nums = [0]*257
for _ in range(N):
    for n in list(map(int, input().split())):
        nums[n] += 1

answer_time, answer_h = sys.maxsize, 0
for h in range(257):
    now_time, now_block = 0, B
    for i in range(257):
        if not nums[i]: continue
        if i < h:
            now_time += (h-i)*nums[i]
            now_block -= (h-i)*nums[i]
        else:
            now_time += ((i-h)*2)*nums[i]
            now_block += (i-h)*nums[i]

    if now_block >= 0 and now_time <= answer_time:
        answer_time = now_time
        answer_h = h

print(answer_time, answer_h)
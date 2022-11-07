# def calc(x, y):
#
#     global min_num
#
#     if y == N:
#         if x < min_num:
#             min_num = x
#         return
#
#     for i in range(len(num_list)):
#         if x < min_num and y+num_list[i] <= N:
#             calc(x+1, y+num_list[i])
#
# N = int(input())
#
# n = 1
#
# min_num = N
#
# num_list = [n**2 for n in range(int(N**(1/2)), 0, -1)]
#
# calc(0, 0)
#
# print(min_num)


N = int(input())

num_list = [n for n in range(N+1)]

for i in range(1, N+1):
    for j in range(1, i):
        if j*j > i:
            break
        if num_list[i] > num_list[i-j*j]+1:
            num_list[i] = num_list[i-j*j]+1

print(num_list[N])
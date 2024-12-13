# import sys
# input = sys.stdin.readline

# N = int(input())
# lst = [1, 0]
# for i in range(2, N+1):
#     lst[0], lst[1] = sum(lst)%10, lst[0]

# print(sum(lst)%10)


import sys
input = sys.stdin.readline

N = int(input())
no, yes = 1, 0
for i in range(2, N+1):
    no, yes = (no+yes)%10, no

print((no+yes)%10)
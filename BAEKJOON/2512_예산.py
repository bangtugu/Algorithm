# import sys
#
# N = int(sys.stdin.readline())
# lst = list(map(int, sys.stdin.readline().split()))
# top = int(sys.stdin.readline())
#
# if sum(lst) <= top:
#     print(max(lst))
# else:
#     gap = sum(lst) - top
#     lst.sort(reverse=True)
#     n = 1
#     gap -= lst[0] - lst[1]
#     isall = False
#     while gap > 0:
#
#         n += 1
#
#         if n == len(lst)-1:
#             isall = True
#             break
#
#         gap -= (lst[n]-lst[n+1]) * n
#
#     if isall:
#         print(top//len(lst))
#     else:
#         print((top - sum(lst[n:]))//n)
        
# 100퍼센트까지 가서 틀렸다그럼 ㅠ

import sys
input = sys.stdin.readline

N = int(input())
lst = int(input())
cost = int(input())

s = cost//N
e = max(lst)


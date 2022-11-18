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

N = int(input())
lst = list(map(int, input().split()))
cost = int(input())

s = cost//N
e = max(lst)

if sum(lst) <= cost:
    print(max(lst))
else:
    while s <= e:

        middle = (s+e)//2

        now_cost = 0

        for money in lst:
            if money < middle:
                now_cost += money
            else:
                now_cost += middle

        if now_cost > cost:
            e = middle - 1
        else:
            s = middle + 1

    print(e)
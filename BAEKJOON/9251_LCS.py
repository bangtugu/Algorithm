# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(1500)

# str1 = input().split()[0]
# str2 = input().split()[0]
# sett = set(list(str1)) & set(list(str2))


# def new_string(string):
#     new_one = ''
#     for i in range(len(string)):
#         if string[i] in sett:
#             new_one += string[i]
    
#     return new_one


# str1 = new_string(str1)
# str2 = new_string(str2)


# def finding(i1, i2, n):
#     if i1 >= len(str1) or i2 >= len(str2): return n
    
#     nn = n
#     for i in range(i2, len(str2)):
#         if min(len(str1)-i1, len(str2)-i) <= nn - n: break
#         if str2[i] == str1[i1]:
#             nn = max(nn, finding(i1+1, i+1, n+1))
#     if min(len(str1)-i1, len(str2)-i2) > nn - n:
#         nn = max(nn, finding(i1+1, i2, n))

#     return nn


# print(finding(0, 0, 0))


'''
시간초과
'''

# import sys
# input = sys.stdin.readline
# from collections import deque

# str1 = '1' + input().split()[0]
# str2 = '2' + input().split()[0]
# lst = [[0]*len(str1) for _ in range(len(str2))]

# Q = deque([[0, 0, 1, 1]])
# answer = 0
# while Q:
#     i1, j1, i2, j2 = Q.popleft()
#     if i2 >= len(str1) or j2 >= len(str2): continue
    
#     if str1[i2] == str2[j2]:
#         lst[i2][j2] = max(lst[i2][j2], lst[i1][j1] + 1)
#         answer = max(answer, lst[i2][j2])
#         Q.append([i2, j2, i2+1, j2+1])
#     else:
#         Q.append([i1, j1, i2+1, j2])
#         Q.append([i1, j1, i2, j2+1])

# print(answer)


'''
시간초과22
'''


import sys
input = sys.stdin.readline

str1 = '1' + input().split()[0]
str2 = '2' + input().split()[0]
lst = [[0]*len(str2) for _ in range(len(str1))]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            lst[i][j] = lst[i-1][j-1]+1
        else:
            lst[i][j] = max(lst[i][j-1], lst[i-1][j], lst[i-1][j-1])

print(lst[-1][-1])
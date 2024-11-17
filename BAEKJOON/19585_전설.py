# import sys
# input = sys.stdin.readline

# C, N = map(int, input().split())
# color_dic = {'end': 0}
# name_dic = {}


# for _ in range(C):
#     string = input().split()[0]
#     target = color_dic
#     for i in range(len(string)):
#         if string[i] not in target: target[string[i]] = {'end': 0}
#         target = target[string[i]]
#     target['end'] += 1

# for _ in range(N):
#     string = input().split()[0]
#     length = len(string)
#     if length not in name_dic: name_dic[length] = {}
#     target = name_dic[length]
#     for i in range(len(string)):
#         if string[i] not in target: target[string[i]] = {}
#         target = target[string[i]]


# def name_check(i, string):
#     if i not in name_dic: return False
#     target = name_dic[i]
#     for i in range(len(string)):
#         if string[i] not in target: return False
#         target = target[string[i]]
#     else:
#         return True

# def can_win(string):
#     c_target = color_dic
#     for i in range(len(string)):
#         if c_target:
#             if c_target['end']:
#                 if name_check(len(string)-i, string[i:]):
#                     return True
#             if string[i] in c_target:
#                 c_target = c_target[string[i]]
#             else:
#                 c_target = 0
        
#         if not c_target:
#             return False

#     return False


# Q = int(input())
# for _ in range(Q):
#     string = input().split()[0]
#     if can_win(string):
#         print('Yes')
#     else:
#         print('No')



import sys
input = sys.stdin.readline

C, N = map(int, input().split())
color_dic = {'end': 0}
name_set = set()


for _ in range(C):
    string = input().split()[0]
    target = color_dic
    for i in range(len(string)):
        if string[i] not in target: target[string[i]] = {'end': 0}
        target = target[string[i]]
    target['end'] += 1

for _ in range(N):
    string = input().split()[0]
    name_set.add(string)


def can_win(string):
    c_target = color_dic
    for i in range(len(string)):
        if c_target:
            if c_target['end']:
                if string[i:] in name_set:
                    return True
            if string[i] in c_target:
                c_target = c_target[string[i]]
            else:
                c_target = 0
        
        if not c_target:
            return False

    return False


Q = int(input())
for _ in range(Q):
    string = input().split()[0]
    if can_win(string):
        print('Yes')
    else:
        print('No')
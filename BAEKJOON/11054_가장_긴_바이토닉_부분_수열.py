import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
ASC_lst = [0]*N
DESC_lst = [0]*N


def binary(s, e, v, lst):
    while s <= e:
        m = (s+e)//2
        if lst[m] == v:
            return m
        if lst[m] >= v:
            e = m-1
        else:
            s = m+1
    
    return s


temp = []
for i in range(N):
    now = lst[i]

    if not temp:
        temp.append(now)
        ASC_lst[i] = 1
    elif now > temp[-1]:
        temp.append(now)
        ASC_lst[i] = len(temp)
    else:
        idx = binary(0, len(temp)-1, now, temp)
        temp[idx] = now
        ASC_lst[i] = idx+1

temp = []
for i in range(N-1, -1, -1):
    now = lst[i]

    if not temp:
        temp.append(now)
        DESC_lst[i] = 1
    elif now > temp[-1]:
        temp.append(now)
        DESC_lst[i] = len(temp)
    else:
        idx = binary(0, len(temp)-1, now, temp)
        temp[idx] = now
        DESC_lst[i] = idx+1

answer = 0
for i in range(N):
    answer = max(answer, ASC_lst[i]+DESC_lst[i]-1)

print(answer)



# import sys
# input = sys.stdin.readline

# N = int(input())
# lst = list(map(int, input().split()))


# def binary(s, e, v, lst):
#     while s <= e:
#         m = (s+e)//2
#         if lst[m] == v:
#             return m
#         if lst[m] >= v:
#             e = m-1
#         else:
#             s = m+1
    
#     return s


# def get_lst(lst):
#     return_lst = [0]*N
#     temp = []
#     for i in range(N):
#         now = lst[i]

#         if not temp:
#             temp.append(now)
#             return_lst[i] = 1
#         elif now > temp[-1]:
#             temp.append(now)
#             return_lst[i] = len(temp)
#         else:
#             idx = binary(0, len(temp)-1, now, temp)
#             temp[idx] = now
#             return_lst[i] = idx+1

#     return return_lst


# ASC_lst = get_lst(lst)
# DESC_lst = list(reversed(get_lst(list(reversed(lst)))))
# answer = 0
# for i in range(N):
#     answer = max(answer, ASC_lst[i] + DESC_lst[i] - 1)

# print(answer)
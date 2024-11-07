import sys
input = sys.stdin.readline

M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]


def convert(lst):
    sorted_lst = sorted(list(set(lst)))
    dic = {}

    for i in range(len(sorted_lst)):
        dic[sorted_lst[i]] = i+1
    
    for i in range(len(lst)):
        lst[i] = dic[lst[i]]
    
    return str(lst)


dic = {}
for i in range(M):
    lst[i] = convert(lst[i])
    if lst[i] not in dic: dic[lst[i]] = 0
    dic[lst[i]] += 1

answer = 0
for key in dic.keys():
    if dic[key] > 1:
        answer += (dic[key] * (dic[key]-1))//2

print(answer)
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(1000) # 재귀시 사용

N = int(input())
str_lst = [input() for _ in range(N)]
cnt = 0
idx_dic = {}
temp = []
can_zero = []

for string in str_lst:
    M = len(string)
    for i in range(M-1):
        alp = string[-2-i]
        if alp not in idx_dic.keys():
            idx_dic[alp] = cnt
            cnt += 1
            temp.append(0)
            can_zero.append(True)
        idx = idx_dic[alp]
        temp[idx] += 10**i
    can_zero[idx_dic[string[0]]] = False

if len(temp) == 10:
    min_alp = []
    for i in range(10):
        if not can_zero[i]: continue
        if not min_alp or temp[i] < min_alp[1]:
            min_alp = [i, temp[i]]
    temp[min_alp[0]] = 0

answer = 0
temp.sort(reverse=True)
for i in range(len(temp)):
    answer += (9-i)*temp[i]
print(answer)
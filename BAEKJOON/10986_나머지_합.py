import sys
input = sys.stdin.readline
# sys.setrecursionlimit(1000) # 재귀시 사용

N, M = map(int, input().split())
num_lst = list(map(int, input().split()))
cnt_dic = {}

for i in range(N):
    if i != 0: num_lst[i] += num_lst[i-1]
    num_lst[i] %= M
    if num_lst[i] in cnt_dic.keys():
        cnt_dic[num_lst[i]] += 1
    else:
        cnt_dic[num_lst[i]] = 0

if 0 in cnt_dic.keys() and cnt_dic[0]:
    cnt_dic[0] += 1

answer = 0
for key in cnt_dic.keys():
    answer += sum(range(cnt_dic[key]+1))

print(answer)
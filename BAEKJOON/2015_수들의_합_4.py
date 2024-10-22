import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

temp = 0
sum_dic = {0: 1}

answer = 0
for i in range(N):
    temp += lst[i]

    if temp-K in sum_dic:
        answer += sum_dic[temp-K]
    
    if temp not in sum_dic: sum_dic[temp] = 0
    sum_dic[temp] += 1

print(answer)


'''
4 0
2 -2 2 -2
'''
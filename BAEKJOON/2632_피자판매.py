import sys
input = sys.stdin.readline

wanted = int(input())
M, N = map(int, input().split())

A = [int(input()) for _ in range(M)]
B = [int(input()) for _ in range(N)]


def pizza(lst):
    total = sum(lst)
    dic = {total : 1,
           0: 1}
    n = len(lst)

    for i in range(n):
        temp = 0
        for j in range(n//2):
            if not n%2 and j == n//2 - 1 and i >= n//2: continue
            temp += lst[(i+j)%n]
            if temp not in dic: dic[temp] = 0
            if total-temp not in dic: dic[total-temp] = 0
            dic[temp] += 1
            dic[total-temp] += 1

    return dic


A_dic = pizza(A)
B_dic = pizza(B)

answer = 0
for key in A_dic:
    if wanted-key in B_dic:
        answer += A_dic[key]*B_dic[wanted-key]

print(answer)
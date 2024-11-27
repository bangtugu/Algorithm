import sys
input = sys.stdin.readline

N = int(input())
limit = list(map(int, input().split()))
lst = []
for i in range(1, N+1):
    p, f, s, v, c = map(int, input().split())
    lst.append([p, f, s, v, c])g

from itertools import combinations

answer = 500*(N+1)
answer_lst = []
for i in range(1, N+1):
    for ca in combinations(list(range(N)), i):
        temp = [0]*5
        for n in ca:
            for j in range(5):
                temp[j] += lst[n][j]
        if temp[-1] > answer: continue

        for j in range(4):
            if temp[j] < limit[j]:
                break
        else:
            if temp[-1] < answer:
                answer = temp[-1]
                answer_lst = list(ca)
            elif temp[-1] == answer:
                answer_lst = sorted([answer_lst, list(ca)])
                answer_lst = answer_lst[0]

if answer_lst:
    print(answer)
    for n in answer_lst:
        print(n+1, end = ' ')
else:
    print(-1)
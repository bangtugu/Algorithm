import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) # 재귀시 사용

'''

2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32

'''

T = int(input())

for tc in range(T):

    K = int(input())
    pages = list(map(int, input().split()))

    table = [[0]*K for _ in range(K)]
    cost = [[0]*K for _ in range(K)]
    for i in range(K):
        table[i][i] = pages[i]

    for j in range(1, K):
        for i in range(K-j):
            table[i][i+j] = min([table[i][i+z]+table[i+z+1][i+j] for z in range(j)])
            cost[i][i+j] = min([cost[i][i+z]+cost[i+z+1][i+j] for z in range(j)])+table[i][i+j]
    
    print(cost[0][K-1])
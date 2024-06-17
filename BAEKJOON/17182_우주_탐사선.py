import sys
input = sys.stdin.readline

N, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

check = [0]*N
check[K] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            table[i][j] = min(table[i][j], table[i][k] + table[k][j])

answer = 1000*N


def dfs(now, cost):
    global answer

    if sum(check) == N:
        answer = min(answer, cost)
        return

    for i in range(N):
        if check[i]: continue
        check[i] = 1
        dfs(i, cost+table[now][i])
        check[i] = 0


dfs(K, 0)
print(answer)

'''
3 0
0 1 30
50 0 50
1 1 1


3 0
0 30 1
1 0 29
28 1 0

4 1
0 83 38 7
15 0 30 83
67 99 0 44
14 46 81 0

'''
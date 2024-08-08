import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
cost = [[-1]*N for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    cost[a][b] = c





answer = N*10000
for i in range(N):
    answer = min(answer, cost[i][N] + cost[N][i])

print(answer)

'''

4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3

'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cost = [[10001]*N for _ in range(N)]

for _ in range(M):
    A, B, C = map(int, input().split())
    cost[A-1][B-1] = min(cost[A-1][B-1], C)
    







'''

3 4
1 2 4
1 3 3
2 3 -1
3 1 -2

'''
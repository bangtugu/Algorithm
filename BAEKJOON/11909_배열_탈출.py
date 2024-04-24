import sys
input = sys.stdin.readline


n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
min_cost = [[0]*n for _ in range(n)]

for y in range(n):
    for x in range(n):
        if y == x == 0: continue
        cost1, cost2 = 10000000, 10000000

        if y > 0:
            cost1 = min_cost[y-1][x] if table[y-1][x] > table[y][x] else min_cost[y-1][x] + table[y][x] - table[y-1][x] + 1
        if x > 0:
            cost2 = min_cost[y][x-1] if table[y][x-1] > table[y][x] else min_cost[y][x-1] + table[y][x] - table[y][x-1] + 1

        min_cost[y][x] = min(cost1, cost2)

print(min_cost[n-1][n-1])
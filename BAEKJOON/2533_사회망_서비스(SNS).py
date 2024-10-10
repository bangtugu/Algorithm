import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000100)

N = int(input())
node = [[] for _ in range(N+1)]
check = [0]*(N+1)
dp = [[0, 0] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)


def find(now):
    check[now] = 1
    for n in node[now]:
        if check[n]: continue
        find(n)
        dp[now][1] += dp[n][0]
        dp[now][0] += min(dp[n])
    dp[now][0] += 1


find(1)
print(min(dp[1]))
'''
8
1 2
1 3
1 4
2 5
2 6
4 7
4 8
'''
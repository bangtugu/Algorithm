import sys
input = sys.stdin.readline
import heapq

N, M, X = map(int, input().split())
cost = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    cost[a].append([c, b])


def find(n):
    lst = [-1]*N
    lst[n] = 0
    Q = [[0, n]]

    while Q:
        v, now = heapq.heappop(Q)

        for c, nex in cost[now]:
            if lst[nex] == -1 or lst[nex] > c+v:
                lst[nex] = c+v
                heapq.heappush(Q, [c+v, nex])

    return lst


return_cost = find(X-1)
answer = 0
for i in range(N):
    if i == X-1: continue
    going_cost = find(i)
    answer = max(answer, going_cost[X-1] + return_cost[i])

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
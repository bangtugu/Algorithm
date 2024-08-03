import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    lst = [1000000001]*N
    lst[i] = 0
    Q = []
    heapq.heappush(Q, [0, i])

    while Q:
        c, idx = heapq.heappop(Q)
        if c > lst[idx]: continue

        for j in range(N):
            nc = c + cost[idx][j]
            if nc < lst[j]:
                lst[j] = nc
                heapq.heappush(Q, [nc, j])
    
    cost[i] = lst

for _ in range(M):
    a, b, c = map(int, input().split())
    if cost[a-1][b-1] <= c:
        print('Enjoy other party')
    else:
        print('Stay here')

'''

5 10
0 4 4 8 7
7 0 7 7 4
1 4 0 5 4
5 2 2 0 7
1 4 1 6 0
1 3 8
2 4 1
4 1 1
1 5 5
3 2 1
3 2 5
4 5 10
5 3 2
1 4 1
1 4 11

'''
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
cost = [[-1]*N for _ in range(N)]
connected = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if cost[a][b] == -1:
        connected[a].append(b)
        cost[a][b] = c
    else:
        cost[a][b] = min(cost[a][b], c)

for i in range(N):
    connected[i].sort(key = lambda x: cost[i][x])

a, b = map(int, input().split())
a -= 1
b -= 1

lst = connected[a][:]
change = True
while change:
    change = False
    temp = []
    for m in lst:
        for j in connected[m]:
            now = cost[a][m] + cost[m][j]
            if cost[a][j] == -1:
                cost[a][j] = now
                temp.append(j)
                change = True
            elif cost[a][b] != -1 and now >= cost[a][b]:
                continue
            elif cost[a][j] > now:
                cost[a][j] = now
                temp.append(j)
                change = True

    lst = temp[:]

print(cost[a][b])


'''

5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5

'''
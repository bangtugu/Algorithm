import sys
input = sys.stdin.readline
from heapq import heappush, heappop

V, E, P = map(int, input().split())
nodes = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])

for i in range(1, V+1):
    nodes[i].sort(key = lambda x: x[1])


def path_find(a, b):
    check = [-1] * (V+1)
    check[a] = 0
    HQ = []
    heappush(HQ, [0, a])

    while HQ:
        nowv, now = heappop(HQ)
        if nowv < check[now]: continue

        for n, v in nodes[now]:
            if check[n] == -1 or nowv + v < check[n]:
                check[n] = nowv + v
                heappush(HQ, [check[n], n])

    return check[b]


if path_find(1, P) + path_find(P, V) <= path_find(1, V):
    print('SAVE HIM')
else:
    print('GOOD BYE')


'''
6 7 4
1 2 1
1 3 1
2 3 10
3 4 1
3 5 2
4 5 1
5 6 1

'SAVE HIM'


6 7 4
1 2 1
1 3 1
2 3 10
3 4 1
3 5 2
4 5 1
5 6 1

'GOOD BYE'
'''
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
node = [[] for _ in range(N+1)]


def get_log(n):
    cnt = 0
    while n:
        n //= 2
        cnt += 1

    return cnt


log = get_log(N)
for _ in range(N-1):
    a, b, c = map(int, input().split())
    node[a].append([b, c])
    node[b].append([a, c])

p = [[0]*log for _ in range(N+1)]
p[1][0] = 1
depth = [-1]*(N+1)
depth[1] = 0
length = [-1]*(N+1)
length[1] = 0

Q = deque([1])
while Q:
    now = Q.popleft()

    for b, c, in node[now]:
        if depth[b] != -1: continue
        p[b][0] = now
        length[b] = length[now]+c
        depth[b] = depth[now]+1
        Q.append(b)

for j in range(1, log):
    for i in range(1, N+1):
        p[i][j] = p[p[i][j-1]][j-1]


def get_p(a, b):
    if depth[b] < depth[a]:
        a, b = b, a
    
    gap = depth[b]-depth[a]
    
    for i in range(log-1, -1, -1):
        if gap >= 2**i:
            b = p[b][i]
            gap -= 2**i

    if a != b:
        for i in range(log-1, -1, -1):
            if p[a][i] != p[b][i]:
                a, b = p[a][i], p[b][i]
        a = p[a][0]

    return a


M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    m = get_p(a, b)
    print(length[a] + length[b] - 2*length[m])
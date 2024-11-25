import sys
input = sys.stdin.readline

N = int(input())
power = [0] + [int(input()) for _ in range(N)]
nodes = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])

p = [[0, 0] for _ in range(N+1)]
p[1] = [1, 0]
answer = [0]*(N+1)
answer[1] = 1

from collections import deque
Q = deque()
Q.append([1, 0])

while Q:
    now, cost = Q.popleft()

    for node, length in nodes[now]:
        if p[node][0]: continue
        p[node] = [now, length]
        Q.append([node, cost+length])
        if cost+length <= power[node]:
            answer[node] = 1
        else:
            temp = power[node]
            answer[node] = node
            while temp >= p[answer[node]][1]:
                temp -= p[answer[node]][1]
                answer[node] = p[answer[node]][0]

for i in range(1, N+1):
    print(answer[i])
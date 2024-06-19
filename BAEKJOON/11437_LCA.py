import sys
input = sys.stdin.readline
sys.setrecursionlimit(55000) # 재귀시 사용

N = int(input())

temp = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    temp[a].append(b)
    temp[b].append(a)

check = [0]*(N+1)
p_lst = [0]*(N+1)
depth = [0]*(N+1)
depth[1] = 1


def get_p(now):
    check[now] = 1

    for node in temp[now]:
        if check[node]: continue
        p_lst[node] = now
        depth[node] = depth[now]+1
        get_p(node)


get_p(1)

M = int(input())
temp = [list(map(int, input().split())) for _ in range(M)]

for a, b in temp:
    check = set([a, b])
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = p_lst[a]
        else:
            b = p_lst[b]
    while a != b:
        a = p_lst[a]
        b = p_lst[b]
    
    print(a)
from collections import deque


def dfs(n):
    v[n] = 1
    lst.append(n)
    for i in range(1, N+1):
        if table[n][i] and not v[i]:
            dfs(i)

def bfs(n):
    Q = deque()
    v = [0] * (N + 1)
    v[n] = 1
    Q.append(n)
    lst = []
    while Q:
        now = Q.popleft()
        lst.append(now)
        for i in range(1, N + 1):
            if table[now][i] and not v[i]:
                Q.append(i)
                v[i] = 1

    print(*lst)


N, M, V = map(int, input().split())
table = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    n1, n2 = map(int, input().split())
    table[n1][n2] = 1
    table[n2][n1] = 1

v = [0] * (N+1)
lst = []

dfs(V)
print(*lst)

bfs(V)
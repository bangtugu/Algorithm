import sys
input = sys.stdin.readline

N = int(input())
p = [-1]*(N+1)
c = [[-1, -1] for _ in range(N+1)]
for _ in range(N):
    i, l, r = map(int, input().split())
    if l != -1:
        c[i][0] = l
        p[l] = c
    if r != -1:
        c[i][1] = r
        p[r] = c

lst = [-1]
for i in range(1, N+1):
    if p[i] == -1:
        root = i


def dfs(n, d):
    if c[n][0] != -1:
        dfs(c[n][0], d+1)
    lst.append(d)
    if c[n][1] != -1:
        dfs(c[n][1], d+1)


dfs(root, 1)
answer = [[0, 0, 0]]

for i in range(1, N+1):
    if len(answer) < lst[i]+1:
        for _ in range(lst[i]-len(answer)+1):
            answer.append([len(answer), N, 1])
    now = lst[i]
    answer[now][1] = min(answer[now][1], i)
    answer[now][2] = max(answer[now][2], i)

answer = sorted(answer[1:], key = lambda x: [-x[2]+x[1], x[0]])
print(answer[0][0], answer[0][2]-answer[0][1]+1)
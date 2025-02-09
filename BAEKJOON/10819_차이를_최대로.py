import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
check = [0]*N
answer = 0


def dfs(n, v):
    if sum(check) == N:
        global answer
        answer = max(answer, v)
        return

    for i in range(N):
        if check[i]: continue
        check[i] = 1
        dfs(lst[i], v + abs(n-lst[i]))
        check[i] = 0


for i in range(N):
    check[i] = 1
    dfs(lst[i], 0)
    check[i] = 0

print(answer)
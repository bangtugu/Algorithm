import sys
input = sys.stdin.readline

N = int(input())
prices = [list(map(int, list(input().split()[0]))) for _ in range(N)]

bicheck = [0]*N
bicheck[0] = 1
check = {}
check[1] = [-1]*N
check[1][0] = 0
answer = 0


def dfs(n, cnt, binum):
    global answer
    answer = max(cnt, answer)

    for i in range(1, N):
        c = prices[n][i]
        if bicheck[i] or check[binum][n] > c: continue
        temp = binum + 2**(i)
        if temp not in check: check[temp] = [-1]*N
        if check[temp][i] != -1 and c >= check[temp][i]: continue
        check[temp][i] = c
        bicheck[i] = 1
        dfs(i, cnt+1, temp)
        bicheck[i] = 0


dfs(0, 1, 1)
print(answer)
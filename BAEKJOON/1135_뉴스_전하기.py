import sys
input = sys.stdin.readline

N = int(input())
Plst = list(map(int, input().split()))
Clst = [[] for _ in range(N)]

for i in range(N):
    if Plst[i] == -1: continue
    Clst[Plst[i]].append(i)


def dfs(n):
    if not Clst[n]: return 0

    temp = sorted([dfs(Clst[n][i]) for i in range(len(Clst[n]))], reverse = True)
    for i in range(len(temp)):
        temp[i] += i+1

    return max(temp)


answer = dfs(0)
print(answer)
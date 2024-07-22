import sys
input = sys.stdin.readline
sys.setrecursionlimit(1500)


def gs(n):
    while group[n] != n:
        n = group[n]
    return n


def find():
    answer = 0

    lst = []
    for i in range(N):
        for j in range(i+1, N):
            lst.append([cost[i][j], i, j])
    
    lst.sort()

    for c, i, j in lst:
        gi = gs(i)
        gj = gs(j)
        if gi == gj: continue
        answer += c
        if gi < gj:
            group[gj] = gi
        else:
            group[gi] = gj

    return answer
    

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
group = list(range(N))
print(find())
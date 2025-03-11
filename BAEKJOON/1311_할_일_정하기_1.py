import sys
input = sys.stdin.readline

N = int(input())
work = [list(map(int, input().split())) for _ in range(N)]
answer = [10000*N]*(1<<N)
answer[0] = 0


for i in range(1<<N):
    k = 0
    for j in range(N):
        if i & (1<<j):
            k += 1
    for j in range(N):
        if not i & (1<<j) and answer[i|1<<j] > answer[i] + work[k][j]:
            answer[i|1<<j] = answer[i] + work[k][j]


print(answer[-1])
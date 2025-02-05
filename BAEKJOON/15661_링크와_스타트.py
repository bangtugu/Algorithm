import sys
input = sys.stdin.readline

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
team = [1] + [0]*(N-1)
answer = sum([sum(line) for line in table])


def checking():
    global answer
    t1 = []
    t2 = []
    for i in range(N):
        if team[i]: t1.append(i)
        else: t2.append(i)
    
    v1 = 0
    for i in t1:
        for j in t1:
            v1 += table[i][j]

    v2 = 0
    for i in t2:
        for j in t2:
            v2 += table[i][j]
    
    answer = min(answer, abs(v1-v2))


def group(i):
    if i == N:
        checking()
        return
    team[i] = 1
    group(i+1)
    team[i] = 0
    group(i+1)


group(1)
print(answer)
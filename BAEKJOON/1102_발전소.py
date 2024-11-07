import sys
input = sys.stdin.readline

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
temp = input().split()[0]
P = int(input())

on = 0
for i in range(N):
    if temp[i] == 'Y':
        on += 1
check = {temp : 0}


def connecting(string, cnt):
    global answer
    if check[string] >= answer: return
    if cnt >= P:
        answer = min(answer, check[string])
        return

    for j in range(N):
        if string[j] == 'Y': continue
        min_cost = 36
        for i in range(N):
            if string[i] == 'N': continue
            min_cost = min(min_cost, costs[i][j])
        
        string2 = string[:j] + 'Y' + string[j+1:]
        if string2 not in check or check[string2] > check[string]+min_cost:
            check[string2] = check[string]+min_cost
            connecting(string2, cnt+1)


if on >= P:
    print(0)
elif not on:
    print(-1)
else:
    answer = N*36
    connecting(temp, on)
    print(answer)

'''

3
0 10 11
10 0 12
12 13 0
NNN
0

0

'''
import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N+2)]

    canmove = [[0]*(N+2) for _ in range(N+2)]

    for i in range(N+2):
        for j in range(i+1, N+2):
            if abs(lst[i][0] - lst[j][0]) + abs(lst[i][1] - lst[j][1]) > 1000: continue
            canmove[i][j] = 1
            canmove[j][i] = 1

    sett = set([0])
    lst = [0]
    idx = 0
    
    while idx < len(lst):
        now = lst[idx]

        for go in range(N+2):
            if go in sett: continue
            if canmove[now][go]:
                canmove[0][go] = 1
                lst.append(go)
                sett.add(go)

        idx += 1

    print('happy' if canmove[0][-1] else 'sad')

'''

2
2
0 0
1000 0
1000 1000
2000 1000
2
0 0
1000 0
2000 1000
2000 2000

'''
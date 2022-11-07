def road(s, e):

    for i in range(n):
        if table[i][s] == 1 and table[i][e] == 0:               # s에 도달 가능한 인자들 e로 연결하기
            table[i][e] = 1


n = int(input())

table = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if table[i][j]:
            road(i, j)

for i in range(n):
    for j in range(n):
        print(table[i][j], end=' ')
    print()
import sys
input = sys.stdin.readline
from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

T = int(input())
for tc in range(T):
    h, w = map(int, input().split())
    table = [input().split()[0] for _ in range(h)]
    key = list(input())
    key = set() if key[0] == '0' else set(key)
    door = {}
    check = [[0]*w for _ in range(h)]


    def control(y, x):

        check[y][x] = 1
        if table[y][x] == '.':
            Q.append([y, x])
        elif table[y][x] == '$':
            Q.append([y, x])
        elif 65 <= ord(table[y][x]) <= 90:
            k = chr(ord(table[y][x])+32)
            if k in key: Q.append([y, x])
            else:
                if k not in door: door[k] = []
                door[k].append([y, x])
        elif 97 <= ord(table[y][x]) <= 122:
            Q.append([y, x])
            k = table[y][x]
            key.add(k)
            if k in door:
                for ny, nx in door[k]:
                    Q.append([ny, nx])
                door[k] = []
        
        return 0

    
    answer = 0
    Q = deque()
    for i in range(h):
        for j in [0, w-1]:
            answer += control(i, j)
    for j in range(1, w-1):
        for i in [0, h-1]:
            answer += control(i, j)

    while Q:
        y, x = Q.popleft()
        if table[y][x] == '$': answer += 1

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or nx < 0 or ny >= h or nx >= w or check[ny][nx] or table[ny][nx] == '*': continue
            answer += control(ny, nx)

    print(answer)



'''
3
5 17
*****************
.............**$*
*B*A*P*C**X*Y*.X.
*y*x*a*p**$*$**$*
*****************
cz
5 11
*.*********
*...*...*x*
*X*.*.*.*.*
*$*...*...*
***********
0
7 7
*ABCDE*
X.....F
W.$$$.G
V.$$$.H
U.$$$.J
T.....K
*SQPML*
irony
'''
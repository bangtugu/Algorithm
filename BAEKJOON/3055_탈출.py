import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
mapp = [[-1]*C for _ in range(R)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
ty, tx = 0, 0
lst1 = []
lst2 = []

for i in range(R):
    temp = input()
    for j in range(C):
        if temp[j] == 'S':
            mapp[i][j] = 0
            lst1.append([i, j])
            continue
        elif temp[j] == '*':
            lst2.append([i, j])
        mapp[i][j] = temp[j]

can_move = False
cnt = 0
while not can_move and lst1:
    temp1 = []
    temp2 = []

    for y, x in lst1:
        if mapp[y][x] == '*': continue
        for d in range(4):
            ny, nx = y+dy[d], x+dx[d]

            if ny < 0 or nx < 0 or ny >= R or nx >= C: continue
            if mapp[ny][nx] == 'D': can_move = mapp[y][x] + 1
            if mapp[ny][nx] != '.': continue
            mapp[ny][nx] = mapp[y][x] + 1
            temp1.append([ny, nx])

    for y, x in lst2:
        for d in range(4):
            ny, nx = y+dy[d], x+dx[d]

            if ny < 0 or nx < 0 or ny >= R or nx >= C: continue
            if mapp[ny][nx] == '*' or mapp[ny][nx] == 'D' or mapp[ny][nx] == 'X': continue
            mapp[ny][nx] = '*'
            temp2.append([ny, nx])

    lst1 = temp1
    lst2 = temp2

if can_move:
    print(can_move)
else:
    print('KAKTUS')
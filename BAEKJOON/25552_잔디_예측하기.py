import sys
input = sys.stdin.readline
# sys.setrecursionlimit(1000) # 재귀시 사용

'''
3 3
XXX
OXX
XXO
1
XOO
OXO
OXO
'''

N, M = map(int, input().split())
start = [list(input()) for _ in range(N)]
D = int(input())
end = [list(input()) for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


end_group = [[0]*M for _ in range(N)]
elst = [0]
cnt = 0
for i in range(N):
    for j in range(M):
        if end_group[i][j]: continue
        if start[i][j] == 'O' and end[i][j] == 'X': continue
        if end[i][j] == 'X': continue

        elst.append(0)
        cnt += 1
        end_group[i][j] = cnt
        temp = [[i, j]]
        idx = 0
        while idx < len(temp):
            y, x = temp[idx]
            if start[y][x] == 'O': elst[cnt] = 1
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if nx < 0 or nx >= M or ny < 0 or ny >= N or end[ny][nx] == 'X' or end_group[ny][nx]: continue
                end_group[ny][nx] = cnt
                temp.append([ny, nx])
            
            idx += 1

check_lst = []
for i in range(N):
    for j in range(M):
        if not end_group[i][j] or elst[end_group[i][j]]: continue
        check_lst.append([i, j])

while True:
    temp = sum(elst)
    
    for y, x in check_lst:
        if elst[end_group[y][x]]: continue

        for i in range(-D, D+1):
            if elst[end_group[y][x]]: break
            ny = y + i
            if ny < 0 or ny >= N: continue
            for j in range(-(D-i) if i >= 0 else -(D+i), D-i+1 if i >= 0 else D+i+1):
                nx = x + j
                if nx < 0 or nx >= M or not elst[end_group[ny][nx]]: continue
                elst[end_group[y][x]] = 1
                break

    if temp == sum(elst): break

if sum(elst) == cnt:
    print('YES')
else:
    print('NO')

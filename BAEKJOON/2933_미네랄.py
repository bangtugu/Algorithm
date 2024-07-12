import sys
input = sys.stdin.readline
from collections import deque

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
R, C = map(int, input().split())


def is_float(y, x): # 떠있는지 확인하는 함수
    check[y][x] = 1
    Q = deque([[y, x]])
    while Q:
        y, x = Q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or ny >= R or nx < 0 or nx >= C or not table[ny][nx] or check[ny][nx]: continue
            if ny == R-1: return False # 해당 미네랄 그룹에 바닥(R-1)에 해당하는 미네랄이 있으면 return False
            check[ny][nx] = 1
            Q.append([ny, nx])

    return True # 이 그룹은 공중에 떠있다.


def fall(y, x):
    check[y][x] = 2 # is_float 함수에서 공중에 떠있는 미네랄 그룹의 경우 check 2차원 리스트에 모두 1로 저장되어있음.
    lst = [[y, x]]
    i = 0
    while i < len(lst):
        y, x = lst[i]
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or ny >= R or nx < 0 or nx >= C or not table[ny][nx] or check[ny][nx] == 2: continue
            check[ny][nx] = 2 # 연결된 미네랄 모두 2로 변경 및 lst에 좌표 저장
            lst.append([ny, nx])
        i += 1
    
    fall_h = R
    for x in range(C): # 모든 가로칸에 대해
        for y in range(R-1, -1, -1): # 떨어질 미네랄 그룹의 가장 낮은 좌표 선택
            if check[y][x] != 2: continue
            for s in range(1, R): # 바닥 or 밑 미네랄까지의 거리 구하기
                if y+s >= R or table[y+s][x] == 1:
                    s -= 1
                    break
            fall_h = min([fall_h, s])
            break # 가장 밑에꺼 이외에는 필요없음.

    for y, x in lst:
        table[y][x] = 0
    for y, x in lst:
        table[y+fall_h][x] = 1


table = []
for _ in range(R):
    line = input()
    lst = []
    for a in line:
        if a == '.': lst.append(0)
        elif a == 'x': lst.append(1)
    table.append(lst)

N = int(input())
y_lst = list(map(int, input().split()))
for t in range(N):

    y = R - y_lst[t]
    if t%2: # 오른쪽에서부터 탐색
        for x in range(C-1, -1, -1):
            if table[y][x]:
                break
        else: continue # 부서지는 미네랄이 없으면 다음 던지기로 넘어가기
    else: # 왼쪽에서부터 탐색
        for x in range(C):
            if table[y][x]:
                break
        else: continue

    check = [[0]*C for _ in range(R)]
    table[y][x] = 0
    for d in range(4): # 부서지는 미네랄의 동서남북 4방향에 대해 미네랄 탐색
        ny = y + dy[d]
        nx = x + dx[d]

        if ny < 0 or ny >= R or nx < 0 or nx >= C or check[ny][nx]: continue # 이미 탐색한 미네랄 그룹이면 패스
        if table[ny][nx] and is_float(ny, nx): # 미네랄이 있고 공중에 떠 있는 상태라면
            fall(ny, nx) # 떨어뜨려주기
            break # 한번에 두 그룹 이상 떨어지는 경우가 없다고 했으니 break.

for i in range(R):
    answer = ''
    for j in range(C):
        if table[i][j]:
            answer += 'x'
        else:
            answer += '.'
    print(answer)
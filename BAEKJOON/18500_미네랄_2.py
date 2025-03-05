import sys
input = sys.stdin.readline

R, C = map(int, input().split())
mapp = [list(input().split()[0]) for _ in range(R)]
N = int(input())
sticks = list(map(int, input().split()))
dy, dx = [-1, 0, 0, 1], [0, 1, -1, 0]


def fall(y, x):
    check = [[0]*C for _ in range(R)]
    check[y][x] = 1
    lst = [(y, x)]
    idx = 0
    while idx < len(lst):
        y, x = lst[idx]
        if y == R-1: return

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or nx < 0 or ny >= R or nx >= C or check[ny][nx] or mapp[ny][nx] == '.': continue
            check[ny][nx] = 1
            lst.append((ny, nx))

        idx += 1
    
    for y, x in lst:
        mapp[y][x] = '.'
    
    dist_to_bottom = R-1
    for y, x in lst:
        for i in range(1, R):
            if i > dist_to_bottom: break
            if y+i >= R or mapp[y+i][x] == 'x': dist_to_bottom = i-1; break
    
    for y, x in lst:
        mapp[y+dist_to_bottom][x] = 'x'


cnt = 0
for i in sticks:
    cnt = (cnt+1)%2
    if cnt:
        for j in range(C):
            if mapp[R-i][j] == 'x':
                mapp[R-i][j] = '.'
                break
        else: continue
    else:
        for j in range(C-1, -1, -1):
            if mapp[R-i][j] == 'x':
                mapp[R-i][j] = '.'
                break
        else: continue
    
    for d in range(4):
        ny = R-i + dy[d]
        nx = j + dx[d]
        if ny < 0 or nx < 0 or ny >= R or nx >= C or mapp[ny][nx] == '.': continue
        fall(ny, nx)

for line in mapp:
    temp = ''
    for a in line:
        temp += a
    print(temp)

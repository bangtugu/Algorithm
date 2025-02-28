import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(N)]
lst = [0]*(N*N-1)
idx = [[0]*N for _ in range(N)]

y, x = N//2, N//2
dy, dx = [0, 1, 0, -1], [-1, 0, 1, 0]
cnt, d = 0, -1
for i in range(4*(N//2)+1):
    l = (i+2)//2
    d = (d + 1)%4
    for _ in range(l):
        y += dy[d]
        x += dx[d]
        if cnt >= N*N-1: break
        idx[y][x] = cnt
        lst[cnt] = mapp[y][x]
        cnt += 1

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
didx = [[0]*(N//2) for _ in range(4)]
y, x = N//2, N//2
for d in range(4):
    for s in range(N//2):
        didx[d][s] = idx[y+dy[d]*(s+1)][x+dx[d]*(s+1)]


def bomb():
    change = 0
    number, cnt = 0, 0
    for i in range(N*N-1):
        if not lst[i]: continue
        if lst[i] == number: cnt += 1
        else:
            if cnt >= 4:
                change += number*cnt
                for j in range(i-1, -1, -1):
                    if lst[j] == number:
                        lst[j] = 0
                        cnt -= 1
                        if not cnt: break
            number, cnt = lst[i], 1
    if cnt >= 4:
        change += number*cnt
        for j in range(N*N-2, -1, -1):
            if lst[j] == number:
                lst[j] = 0
                cnt -= 1
                if not cnt: break
    
    return change


def setting():
    temp = []
    number, cnt = 0, 0
    for i in range(N*N-1):
        if not lst[i]: continue
        if number == lst[i]: cnt += 1
        else:
            if number: temp.extend([cnt, number])
            number, cnt = lst[i], 1
    temp.extend([cnt, number])
    if len(temp) < N*N-1:
        temp = temp + [0]*(N*N-1-len(temp))
    for i in range(N*N-1):
        lst[i] = temp[i]

answer = 0
for _ in range(M):
    d, s = map(int, input().split())

    for i in range(s):
        lst[didx[d-1][i]] = 0
    
    change = 1
    while change:
        change = bomb()
        answer += change
    setting()

print(answer)
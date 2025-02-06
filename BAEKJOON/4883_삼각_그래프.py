import sys
input = sys.stdin.readline

N = int(input())
tc = 0
dy, dx = [0, 1, 1, 1], [1, -1, 0, 1]

while N:
    tc += 1
    table = [list(map(int, input().split())) for _ in range(N)]
    check = [['.']*3 for _ in range(N)]
    check[0][1] = table[0][1]

    for i in range(N):
        for j in range(3):
            if check[i][j] == '.': continue
            for d in range(4):
                ny = i + dy[d]
                nx = j + dx[d]

                if ny < 0 or nx < 0 or ny >= N or nx >= 3: continue
                if check[ny][nx] == '.' or check[ny][nx] > check[i][j] + table[ny][nx]:
                    check[ny][nx] = check[i][j] + table[ny][nx]

    print(str(tc)+'.', check[N-1][1])
    N = int(input())
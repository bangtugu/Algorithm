import sys


input = sys.stdin.readline

table = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

visit = [[0]*5 for _ in range(5)]
idx = 0
lst = [[r, c]]
rocation = [0]*7
visit[r][c] = 1
rocation[0] = [r, c]
while idx < len(lst):
    y, x = lst[idx]
    
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if ny < 0 or nx < 0 or ny >= 5 or nx >= 5 or table[ny][nx] == -1 or visit[ny][nx]: continue

        visit[ny][nx] = 1
        if table[ny][nx] not in [-1, 0]: rocation[table[ny][nx]] = [ny, nx]
        lst.append([ny, nx])

    idx += 1

if 0 in rocation:
    print(-1)
else:
    value_table = [[0]*7 for _ in range(7)]

    for i in range(7):
        for j in range(i+1, 7):
            if i == j or value_table[i][j]: continue

            sy, sx = rocation[i]
            ey, ex = rocation[j]

            idx = 0
            lst = [[sy, sx, 0]]
            visit = [[0]*5 for _ in range(5)]
            visit[sy][sx] = 1
            while idx < len(lst):
                y, x, v = lst[idx]

                if y == ey and x == ex:
                    value_table[i][j] = v
                    value_table[j][i] = v
                    break

                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    nv = v + 1

                    if ny < 0 or nx < 0 or ny >= 5 or nx >= 5 or table[ny][nx] == -1 or visit[ny][nx]: continue

                    visit[ny][nx] = 1
                    lst.append([ny, nx, nv])

                idx += 1

    answer = [10000]


    def check(lst, now, value):
        if sum(lst) == 7:
            answer[0] = min(answer[0], value)
            return
        
        for i in range(1, 7):
            if lst[i]: continue

            lst[i] = 1
            check(lst, i, value+value_table[now][i])
            lst[i] = 0


    check([1, 0, 0, 0, 0, 0, 0], 0, 0)
    print(answer[0])
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def dfs(y, x, n, value):
    if n >= 4:
        global max_num
        if max_num < value:
            max_num = value
        return

    for d in range(4):
        yy = y + dy[d]
        xx = x + dx[d]

        if 0 <= yy < N and 0 <= xx < M and not v[yy][xx]:
            v[yy][xx] = 1
            dfs(yy, xx, n+1, value+table[yy][xx])
            v[yy][xx] = 0


N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]

max_num = 0

for i in range(N):
    for j in range(M):
        v[i][j] = 1
        dfs(i, j, 1, table[i][j])

print(max_num)


'''
dfs로 하니까
 O
OOO
이 모양으로 있는거 고려가 안됨.
'''
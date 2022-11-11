dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def dfs(y, x, n, value):
    global max_sum

    if max_sum >= value + max_num * (4 - n):
        return

    if n >= 4:
        if max_sum < value:
            max_sum = value
        return

    for d in range(4):
        yy = y + dy[d]
        xx = x + dx[d]

        if 0 <= yy < N and 0 <= xx < M and not v[yy][xx]:
            if n == 2:                                              # 2개의 블럭이 선택된 상태에서, 3번째 블록을 선택하고
                v[yy][xx] = 1                                       # 3번째가 아닌 2번째 블록에서 dfs를 한번 더 들어감으로써 뫼산모양 블럭 탐색
                dfs(y, x, n + 1, value + table[yy][xx])
                v[yy][xx] = 0
            v[yy][xx] = 1                                           # 조건문 밖에서 뫼산모양 제외 모든 모양의 블럭을 탐색한다.
            dfs(yy, xx, n + 1, value + table[yy][xx])
            v[yy][xx] = 0


N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]

max_sum = 0

max_num = max(map(max, table))                                      # 가지치기 하기 위해서 가장 큰 값 저장

for i in range(N):
    for j in range(M):
        v[i][j] = 1
        dfs(i, j, 1, table[i][j])                                   # 모든 칸에 대해서 dfs 실행
        v[i][j] = 0

print(max_sum)
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def bfs(ty, tx, t):

    v = [[-1]*N for _ in range(N)]
    v[y][x] = 0

    Q = deque()
    Q.append([y, x, 0])

    while Q:

        ny, nx, n = Q.popleft()

        for i in range(4):

            nny = ny + dy[i]
            nnx = nx + dx[i]

            if 0 <= nny < N and 0 <= nnx < N and sea[nny][nnx] <= age and v[nny][nnx] == -1:
                v[nny][nnx] = 1
                if nny == ty and nnx == tx:
                    return n+1
                if n+1 <= t:
                    Q.append([nny, nnx, n+1])


N = int(input())

sea = [list(map(int, input().split())) for _ in range(N)]

fish = []

age = 2
eat_cnt = 0

y = x = 0

for i in range(N):
    for j in range(N):
        if 1 <= sea[i][j] <= 6:
            fish.append([sea[i][j], i, j])
        if sea[i][j] == 9:
            sea[i][j] = 0
            y = i
            x = j

fish.sort()

cnt = 0

while fish:

    eat_now = -1
    eat_d = N*N
    ey = y
    ex = x

    for i in range(len(fish)):
        if fish[i][0] < age:                # 상어 나이보다 작은 물고기일때
            fy = fish[i][1]                 # 좌표 임시저장
            fx = fish[i][2]
            fd = bfs(fy, fx, eat_d)         # bfs로 먹으러 갈 거리 계산
            if fd:                          # 먹으러갈 수 없을 경우 None이 저장되므로 한번 조건 걸어줌
                if fd < eat_d:              # 거리가 가까우면 갱신
                    eat_now = i
                    eat_d = fd
                    ey = fy
                    ex = fx
                elif fd == eat_d:           # 거리가 같은데
                    if fy < ey:             # 더 위에있으면 갱신
                        eat_now = i
                        eat_d = fd
                        ey = fy
                        ex = fx
                    elif fy == ey:          # 높이는 같은데
                        if fx < ex:         # 더 왼쪽에 있으면 갱신
                            eat_now = i
                            eat_d = fd
                            ey = fy
                            ex = fx

        else:                               # 나이보다 물고기 크기가 커지면 for문 break
            break

    if eat_now == -1:                       # -1이 나오면 먹을수 있는 물고기가 없다는 뜻: while문 break
        break
    else:
        y = ey                  # 상어 위치 갱신
        x = ex
        sea[y][x] = 0           # 먹은 물고기 없애기
        fish.pop(eat_now)       # 리스트에서도
        eat_cnt += 1            
        if eat_cnt >= age:      # 상어 성장
            eat_cnt = 0
            age += 1
        cnt += eat_d            # 결과값 갱신

print(cnt)
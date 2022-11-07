from collections import deque


def canmove():

    for i in range(N):
        for j in range(N):

            y = i
            x = j

            for z in [1, 3]:

                ny = y + dy[z]
                nx = x + dx[z]

                if 0 <= ny < N and 0 <= nx < N and L <= abs(land[y][x] - land[ny][nx]) <= R:
                    return True

    return False


def letsmove():

    unite = [[0] * N for _ in range(N)]                 # 소속 연합 배열
    now_unite = 1                                       # 연합 넘버링
    unite_dict = {}                                     # 연합 인구수 결과 저장 사전

    for i in range(N):
        for j in range(N):

            if not unite[i][j]:                         # 연합 없는 칸을 발견하면
                Q = deque()                             # 주변이랑 연합 이어주는 dfs
                Q.append((i, j))
                unite[i][j] = now_unite

                now_unite_sum = land[i][j]              # 인구수 총합 저장하는 변수
                unite_cnt = 1                           # 나라 수 저장하는 변수

                while Q:

                    y, x = Q.popleft()

                    for z in range(4):

                        ny, nx = y + dy[z], x + dx[z]

                        if 0 <= ny < N and 0 <= nx < N and not unite[ny][nx] and L <= abs(land[y][x] - land[ny][nx]) <= R:
                            unite[ny][nx] = now_unite
                            now_unite_sum += land[ny][nx]
                            unite_cnt += 1
                            Q.append((ny, nx))

                unite_dict[now_unite] = now_unite_sum // unite_cnt          # 인구수 결과 사전에 저장

                now_unite += 1                                              # 연합 넘버링 + 1

    for y in range(N):
        for x in range(N):
            land[y][x] = unite_dict[unite[y][x]]                            # 연합 배정 끝나면 사전에 저장된 값으로 인구수 바꿔주기


N, L, R = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

moving = 0

while canmove():                # 연합이 하나라도 생길 수 있으면

    moving += 1                 # 인구이동 횟수 + 1
    letsmove()                  # 인구이동

print(moving)                   # 횟수 출력


'''
    시간초과
'''
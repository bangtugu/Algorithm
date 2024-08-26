import sys
input = sys.stdin.readline
from collections import deque


def move():

    unite = [[0] * N for _ in range(N)]
    now_unite = 1
    unite_dict = {}

    for i in range(N):
        for j in range(N):
            if unite[i][j]: continue

            for d in range(4):
                ni, nj = i + dy[d], j + dx[d]
                if ni < 0 or nj < 0 or ni >= N or nj >= N: continue
                if unite[ni][nj]: continue
                if L <= abs(land[i][j] - land[ni][nj]) <= R:
                    break
            else:
                continue

            Q = deque()
            Q.append([i, j])
            unite[i][j] = now_unite
            unite_dict[now_unite] = land[i][j]
            unite_cnt = 1

            while Q:
                y, x = Q.popleft()

                for d in range(4):
                    ny, nx = y + dy[d], x + dx[d]

                    if 0 > ny or 0 > nx or ny >= N or nx >= N or unite[ny][nx]: continue
                    if L <= abs(land[y][x] - land[ny][nx]) <= R:
                        unite_dict[now_unite] += land[ny][nx]
                        unite[ny][nx] = now_unite
                        unite_cnt += 1
                        Q.append([ny, nx])

            unite_dict[now_unite]//=unite_cnt
            now_unite += 1

    ismove = False
    for y in range(N):
        for x in range(N):
            if not unite[y][x] or land[y][x] == unite_dict[unite[y][x]]: continue
            ismove = True
            land[y][x] = unite_dict[unite[y][x]]

    return ismove


N, L, R = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

moving = 0
while move():
    moving += 1
    
print(moving)


'''
    시간초과
'''
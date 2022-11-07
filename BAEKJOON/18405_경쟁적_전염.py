import sys
sys.stdin = open('18405_input.txt', 'r')
from collections import deque

T = int(input())

dx = [-1, 0, 1, 0]#좌상우하
dy = [0, -1, 0, 1]

for test_case in range(1, T+1):
    # N, K = map(int, input().split())
    # table = [list(map(int, input().split())) for _ in range(N)]
    # S, Y, X = map(int, input().split())     # 문제에서 행, 열이 X, Y길래 임의로 X, Y 바꿔서 사용
    #
    # v = []                                  # 처음에 바이러스가 있는 좌표, 바이러스 번호 저장
    # for i in range(N):
    #     for j in range(N):
    #         if table[i][j]:
    #             v.append([table[i][j], i, j])
    #
    # Q = deque()
    #
    # for i in range(1, K+1):                 # 바이러스 번호 순서대로 deque에 넣기
    #     for virus in v:
    #         if virus[0] == i:
    #             Q.append((virus[1], virus[2]))
    #
    # Q.append(('cycle', 'cycle'))            # 사이클이 돌았는지 감지할 변수 넣기
    # n = 1                                   # 현재 사이클 번호
    #
    # while Q:                                # 사이클 돌리는 while문
    #     y, x = Q.popleft()
    #     if y == 'cycle':                    # 각 사이클의 가장 오른쪽에 있는 변수가 감지가 되면
    #         if n == S:                      # 원하는 사이클에 도달했다면 while문 종료
    #             break
    #         n += 1                          # 아니라면 사이클 번호 + 1
    #         Q.append(('cycle', 'cycle'))    # 오른쪽에 변수 다시 넣기
    #         continue                        # 바이러스 퍼뜨리는 반복문은 건너뛰기
    #
    #     for i in range(4):                  # 바이러스 퍼뜨리는 반복문
    #         yy = y + dy[i]
    #         xx = x + dx[i]
    #         if 0 <= yy < N and 0 <= xx < N and not table[yy][xx]:
    #             table[yy][xx] = table[y][x]
    #             Q.append((yy, xx))
    #
    # print('#{} {}'.format(test_case, table[Y-1][X-1]))

    N, K = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]
    S, Y, X = map(int, input().split())  # 문제에서 행, 열이 X, Y길래 임의로 X, Y 바꿔서 사용

    '''

        bfs가 아니었네 ㅎㅎ;
        번호가 낮다고 높은 번호의 바이러스를 덮어씌우는게 아니므로,
        결국 처음에 가장 가깝게 배치된 바이러스가 목표 칸을 차지함.
        가장 가깝게 배치된 바이러스가 여러가지일 경우 낮은 번호가 이김.

    '''

    v = [S, K + 1]
    for i in range(N):
        for j in range(N):
            if table[i][j]:  # 좌표에 바이러스가 있다면
                if v[0] == abs(Y - 1 - i) + abs(X - 1 - j):  # 해당 바이러스와 목표의 거리가 저장된것과 같으면
                    v[1] = min(v[1], table[i][j])  # 바이러스 번호만 비교해서 낮은거로 교체
                elif v[0] > abs(Y - 1 - i) + abs(X - 1 - j):  # 거리가 더 짧으면
                    v = [abs(Y - 1 - i) + abs(X - 1 - j), table[i][j]]  # 거리, 번호 모두 교체

    # 기간 내에 목표까지 도달하는 바이러스가 없다면 0 출력
    if v[1] == K + 1:
        print('#{} {}'.format(test_case, 0))
    else:
        print('#{} {}'.format(test_case, v[1]))
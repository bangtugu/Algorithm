import sys
sys.stdin = open('7576_input.txt', 'r')
from collections import deque

dx = [-1, 0, 1, 0]     # 좌상우하
dy = [0, -1, 0, 1]

T = int(input())

for test_case in range(1, T+1):
    M, N = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]

    Q = deque()

    for i in range(N):
        for j in range(M):
            if table[i][j] == 1:   # 처음부터 익어있는 토마토들의 좌표 저장
                Q.append((i, j))

    # 익지 않은 토마토들이 익는데 걸릴 시간을 구하는 while문
    while Q:
        yy, xx = Q.popleft()
        for i in range(4):
            dyy = yy + dy[i]
            dxx = xx + dx[i]
            if 0 <= dyy < N and 0 <= dxx < M and table[dyy][dxx] == 0:  # 아직 익지 않은 토마토의 값을
                table[dyy][dxx] = table[yy][xx] + 1                     # 기존 토마토 + 1 로 변경
                Q.append((dyy, dxx))                                    # 주변 토마토 익혀버리게 deque에 넣어줌.

    max_num = 0
    # 안익은 토마토가 있는지, 다 익었다면 모든 토마토가 익는데에 얼마나 걸렸는지 반환하는 반복문
    for line in table:
        if 0 in line:
            max_num = 0
            break
        max_num = max(max_num, max(line))

    print('{} {}'.format(test_case, max_num-1))
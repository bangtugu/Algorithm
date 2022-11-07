import sys
sys.stdin = open('3184_input.txt', 'r')
from collections import deque


# 한 구역을 확인하고 결과를 리턴할 함수
def check(y, x):
    ds = dw =0      # 구역의 늑대, 양 마릿수 저장하는 변수

    if table[y][x] == 'o':    # 현재 칸이 양이나 늑대라면 변수에 더해줌.
        ds += 1
    elif table[y][x] == 'v':
        dw += 1

    canout = False # 마당을 벗어나는지 판단하는 변수

    Q = deque()
    Q.append([y, x])

    while Q:
        yy, xx = Q.popleft()
        for z in range(4):
            dyy = yy + dy[z]
            dxx = xx + dx[z]
            if dyy < 0 or dyy >= R or dxx < 0 or dxx >= C:      # 마당 범위를 벗어날 경우 else문에 진입하지 않고
                canout = True                                   # canout을 True로 변경함.
            else:
                if not visit[dyy][dxx]:                # 확인한 칸이 아닌 경우
                    visit[dyy][dxx] = 1                # 확인한 칸으로 설정하고
                    if table[dyy][dxx] != '#':         # 울타리가 아니라면
                        Q.append([dyy, dxx])           # deque에 추가
                        if table[dyy][dxx] == 'o':     # 양인지 늑대인지 확인 후 변수에 반영
                            ds += 1
                        elif table[dyy][dxx] == 'v':
                            dw += 1

    if canout:
        ds = dw = 0     # 마당 범위를 벗어날 경우 모두 도망가므로 0마리 리턴
    elif dw >= ds:      # 늑대가 양보다 같거나 많을 경우 양을 0마리로 변경
        ds = 0
    else:               # 양이 더 많을 경우 늑대를 0마리로 변경
        dw = 0

    return ds, dw


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

T = int(input())

for test_case in range(1, T+1):

    R, C = map(int, input().split())
    table = [list(' '.join(input()).split()) for _ in range(R)]

    visit = [[0] * C for _ in range(R)]     # 확인한 칸인지 확인할 리스트

    s = w = 0                 # 늑대, 양 마릿수 저장할 변수

    for i in range(R):
        for j in range(C):

            if not visit[i][j]:       # 확인한 칸이 아닌 경우
                visit[i][j] = 1       # 확인한 칸으로 변경하고

                if table[i][j] != '#':       # 울타리가 아닐 때

                    ds, dw = check(i, j)     # 함수 실행

                    s += ds                  # 함수로부터 얻은 늑대, 양 마릿수 더하기
                    w += dw

    print('#{} {} {}'.format(test_case, s, w))
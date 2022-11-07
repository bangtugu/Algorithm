
def start(y, x, n):
    global can
    if n == 9:                                                      # 대충 n 9 될동안 벽에 안깔리고 살아있으면 벽 다 사라져서 이동 가능
        can = 1

    if can:
        return

    # print(y, x, n)
    
    for i in range(9):
        yy = y + dy[i]
        xx = x + dx[i]

        if 0 <= yy < 8 and 0 <= xx < 8:
                                                                    # #을 직접 하나씩 내리면서 하면 오래걸릴거같아서 n을 빼주는 식으로 구현
            if 0 <= yy-n < 8 and table[yy-n][xx] == '#':            # 해당 시간에 이동할 좌표에 벽이 있으면 불가능
                pass
            else:
                if 0 <= yy-n-1 < 8 and table[yy-n-1][xx] == '#':    # 해당 시간에 이동할 좌표 위에 벽이 있으면 깔려서 안됨
                    pass
                else:
                    start(yy, xx, n+1)                              # 다 괜찮으면 재귀


can = 0

table = [list(input()) for _ in range(8)]

# print(table)

sy, sx = 7, 0

# 상하좌우 대각선 제자리 등 9가지 이동방향
dy = [-1, -1, -1, 0, 1, 1, 1, 0, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1, 0]

start(sy, sx, 0)

print(can)
import sys
sys.stdin = open('2806_input.txt', 'r')


def N_Queen(num):
    global cnt
    # num이 N까지 왔다는 것은 Queen_check을 N번 통과하고 N개의 퀸이 놓여졌단 뜻
    if num == N:
        cnt += 1
        return

    for i in range(N):
        if Queen_check(num, i):
            lst[num][i] = 1
            N_Queen(num+1)
            lst[num][i] = 0


def Queen_check(y, x):
    for i in range(N):
        if lst[i][x] == 1: # 세로에 있는지 확인
            return False

        # 가로는 확인 안해도 될듯?

        # 대각선 4방향에 있는지 확인
        if 0 <= y+i < N and 0 <= x+i < N and lst[y+i][x+i] == 1:
            return False
        if 0 <= y+i < N and 0 <= x-i < N and lst[y+i][x-i] == 1:
            return False
        if 0 <= y-i < N and 0 <= x+i < N and lst[y-i][x+i] == 1:
            return False
        if 0 <= y-i < N and 0 <= x-i < N and lst[y-i][x-i] == 1:
            return False
    
    # 다 해당 안되면 True 반환
    return True


T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    cnt = 0
    lst = [[0] * N for _ in range(N)]
    N_Queen(0)

    print('#{} {}'.format(test_case, cnt))


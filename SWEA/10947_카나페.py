import sys
sys.stdin = open('10947_input.txt', 'r')







# T = int(input())
#
# for test_case in range(1, T+1):
#     N = int(input())
#     t1 = sorted(list(map(int, input().split())))
#     t2 = sorted(list(map(int, input().split())))
#
#     max_V = 0
#     for i in range(N):
#         max_V += t1[i]*t2[i]
#
#     print('#{} {}'.format(test_case, max_V))















def canape(n, summ):

    if n == N:
        global max_V
        if summ > max_V:
            max_V = summ

    for i in range(N):
        if not used[i]:
            used[i] = 1
            canape(n+1, summ + table[0][n] * table[1][i])
            used[i] = 0


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(2)]

    max_V = 0
    used = [0] * N

    canape(0, 0)

    print('#{} {}'.format(test_case, max_V))











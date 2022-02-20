import sys
sys.stdin = open('1865_input.txt', 'r')


def calc(n, per):
    global max_val
    if n == N:
        max_val = per
        return

    for i in range(N):
        if not v[i]:
            if table[n][i] == 0:
                now = 0
            else:
                now = per * table[n][i]/100
            if now > max_val:
                v[i] = 1
                calc(n+1, now)
                v[i] = 0


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    v = [0] * N
    max_val = 0
    calc(0, 100)

    print('#{} {:.6f}'.format(test_case, max_val))
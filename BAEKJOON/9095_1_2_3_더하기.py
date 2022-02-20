import sys
sys.stdin = open('9095_input.txt', 'r')


def check(n):

    if n >= N:
        if n == N:
            global cnt
            cnt += 1
        return

    check(n+1)
    check(n+2)
    check(n+3)


T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    cnt = 0

    check(0)

    print(cnt)
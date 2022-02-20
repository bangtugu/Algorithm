import sys
sys.stdin = open('1980_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    n, m, t = map(int, input().split())

    # 먹는데 더 오래걸리는 햄버거
    L = max(n, m)
    # 덜 걸리는 햄버거
    S = min(n, m)

    SS = t//S
    LL = 0
    t = t % S
    min_cola = [t, SS+LL]

    # t가 0이면 종료
    while t and SS:

        SS -= 1
        t += S

        LL += t // L
        t = t % L

        # t가 가장 낮을 때를 저장
        if t < min_cola[0]:
            min_cola[0] = t
            min_cola[1] = SS + LL

    print('#{} {} {}'.format(test_case, min_cola[1], min_cola[0]))

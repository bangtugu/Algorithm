import sys
sys.stdin = open('10158_input.txt', 'r')


def ant(i, j):
    if (i // j) % 2:
        if i % j:
            i = j - i % j
        else:
            i = j
    else:
        i = i % j

    return i


T = int(input())

for test_case in range(1, T+1):
    w, h = map(int, input().split())
    p, q = map(int, input().split())
    t = int(input())

    p += t
    q += t

    p = ant(p, w)
    q = ant(q, h)

    print(p, q)

    #print('#{} {} {}'.format(test_case, p, q))



    # if (p // w) % 2:
    #     if p % w:
    #         p = w - p % w
    #     else:
    #         p = w
    # else:
    #     p = p % w
    #
    # if (q // h) % 2:
    #     if q % h:
    #         q = h - q % h
    #     else:
    #         q = h
    # else:
    #     q = q % h
    #
    # print(p, q)
    #
    # print('#{} {} {}'.format(test_case, p, q))


    # w, h = map(int, input().split())
    # p, q = map(int, input().split())
    # t = int(input())
    #
    # dx = dy = 1
    #
    # while t:
    #
    #     if p == w or p == 0:
    #         dx *= -1
    #     if q == h or q == 0:
    #         dy *= -1
    #
    #     p += dx
    #     q += dy
    #     t -= 1
    #
    # print(p, q)
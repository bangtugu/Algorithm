import sys
sys.stdin = open('13038_input.txt', 'r')


def start(n):
    day = N // sum(Class) * 7 - 7
    left = N % sum(Class) + sum(Class)

    while left:
        left -= Class[n]
        day += 1
        n = (n+1) % 7

    global min_day
    if day < min_day:
        min_day = day


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    Class = list(map(int, input().split()))

    min_day = 7000000

    for i in range(7):
        if Class[i]:
            start(i)

    print('#{} {}'.format(test_case, min_day))

import sys
sys.stdin = open('21758_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    honey = sum(a[1:-1]) + max(a)

    cut = 1
    while cut < len(a)-1 and a[cut] >= a[cut+1] * 2:
        cut += 1

    honey = max(honey, sum(a[1:] + a[cut+1:]) - a[cut])

    cut = -3
    while cut * (-1) <= len(a)-1 and a[cut+1] >= a[cut] * 2:
        cut -= 1

    honey = max(honey, sum(a[:-1] + a[:cut+1]) - a[cut+1])

    print('#{} {}'.format(test_case, honey))


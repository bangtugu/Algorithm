T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    K = list(map(int, input().split()))

    nope = []

    print('#{}'.format(test_case), end=' ')
    for i in range(1, N + 1):
        if i not in K:
            print(i, end=' ')
    print()

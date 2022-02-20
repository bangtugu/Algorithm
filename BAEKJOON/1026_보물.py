import sys
sys.stdin = open('1026_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort(reverse=True)

    total = 0
    for i in range(N):
        total += A[i] * B[i]


    print('#{} {}'.format(test_case, total))


import sys
sys.stdin = open('2805.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    table = [input() for _ in range(N)]
    total = 0
    j = 0
    for i in range(N):
        for income in table[i][N//2 - j:N - N//2 + j]:
            total += int(income)
        if i < N//2 :
            j += 1
        else:
            j -= 1
    print('#{} {}'.format(test_case, total))


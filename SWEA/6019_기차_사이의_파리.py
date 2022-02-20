import sys
sys.stdin = open('6019_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    D, A, B, F = map(int, input().split())

    distance = D/(A+B)*F

    print('#{} {}'.format(test_case, distance))
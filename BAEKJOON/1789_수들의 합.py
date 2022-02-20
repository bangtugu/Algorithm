import sys
sys.stdin = open('1789_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    # 주어지는 수
    N = int(input())
    count = -1
    while N > 0:
        N -= count + 2 # count(-1) + 2 = 1부터
        count += 1
    print('#{} {}'.format(test_case, count))
import sys
sys.stdin = open('5603_input.txt', 'r')

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    table = []
    total = 0
    for i in range(N):
        numb = int(input())
        table += [numb]
        total += numb
    count = 0
    for i in table:
        if i > total/N:
            count += i - int(total/N)
    print('#{} {}'.format(test_case, count))
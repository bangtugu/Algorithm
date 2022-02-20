import sys
sys.stdin = open('1292_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):

    s, e = map(int, input().split())
    table = []

    i = 1
    while len(table) < e:
        for j in range(i):
            table += [i]
        i += 1

    total = 0
    for i in range(s-1, e):
        total += table[i]


print('#{} {}'.format(test_case, total))
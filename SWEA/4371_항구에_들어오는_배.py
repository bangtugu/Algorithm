import sys
sys.stdin = open('4371_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    # 맨 처음 1 버리기
    one = input()

    # 1 빼고 리스트에 넣기
    table = [int(input())-1 for _ in range(N-1)]
    # table1 = [2, 3] (원래 1, 3, 4)
    # table2 = [6, 9, 12, 18] (원래 1, 7, 10, 13, 19)
    # table3 = [499999999, 999999998] (원래 1, 500000000 999999999)

    i = 0
    while i < len(table):
        j = i+1
        while j < len(table):
            if table[j] % table[i]:# 앞의 숫자로 나누어 떨어지지 않으면
                j += 1
            else:
                table.pop(j)# 앞의 숫자로 나누어떨어지면
        i += 1

    print('#{} {}'.format(test_case, len(table)))
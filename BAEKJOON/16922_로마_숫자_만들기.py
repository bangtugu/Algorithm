import sys
sys.stdin = open('16922_input.txt', 'r')


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    table = [1, 5, 10, 50]
    lst = [1, 5, 10, 50]
    for _ in range(N-1):
        now_lst = []
        for i in range(4):
            for num in lst:
                new_num = num + table[i]
                if new_num not in now_lst:
                    now_lst.append(num+table[i])
        lst = now_lst
    print(lst)
    count = len(lst)

    print('#{} {}'.format(test_case, count))

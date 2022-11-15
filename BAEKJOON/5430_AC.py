'''
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
'''


T = int(input())
for test_case in range(T):
    p = input()
    n = int(input())
    lst = input()
    if n > 0:
        lst = list(map(int, lst[1:-1].split(',')))
    else:
        lst = []
    now_front = True
    now_error = False
    s = 0
    e = len(lst)

    for alp in p:

        if alp == 'R':
            now_front = not now_front

        elif alp == 'D':
            if n == 0:
                now_error = not now_error
                break

            n -= 1

            if now_front:
                s += 1
            else:
                e -= 1

    if now_error:
        print('error')
    elif now_front:
        print(str(lst[s:e]).replace(' ', ''))
    else:
        print(str(list(reversed(lst[s:e]))).replace(' ', ''))
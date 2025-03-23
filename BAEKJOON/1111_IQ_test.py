import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

if N == 1:
    print('A')
elif N == 2:
    if len(set(lst)) == 1:
        print(lst[0])
    else:
        print('A')
else:
    a, b = 0, 0
    for i in range(N-1):
        if not i:
            a = (lst[1]-lst[2])//(lst[0]-lst[1]) if lst[0] != lst[1] else 0
            b = lst[1] - lst[0]*a
        else:
            if lst[i]*a+b != lst[i+1]:
                print('B')
                break
    else:
        print(lst[-1]*a+b)
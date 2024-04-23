import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())
    K = set()
    K.add(1)

    for _ in range(N):
        string = list(input().split())
        temp = set()

        for i in range(0, 4, 2):
            num = int(string[i+1])
            for n in K:
                if string[i] == '+':
                    temp.add((n+num)%7)
                else:
                    temp.add((n*num)%7)
                    
        K = temp

    if 0 in K:
        print('LUCKY')
    else:
        print('UNLUCKY')
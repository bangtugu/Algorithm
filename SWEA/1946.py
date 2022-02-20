import sys
sys.stdin = open('1946_input.txt', 'r')

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    string = ''
    for i in range(N):
        alp = list(input().split())
        string += alp[0]*int(alp[1])

    print('#{}'.format(test_case))
    for i in range(int(len(string)//10)):
        print(string[0:10])
        string = string[10:]
    print(string)
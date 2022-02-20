import sys
sys.stdin = open('1316.txt', 'r')

def isgroup(string):
    alp_list = [string[0]]
    for i in range(len(string)-1):
        if string[i] != string[i+1] and string[i+1] in alp_list:
            return 0
        alp_list.append(string[i+1])
    return 1


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    count = 0
    for i in range(N):
        count += isgroup(input())
    print('#{} {}'.format(test_case, count))
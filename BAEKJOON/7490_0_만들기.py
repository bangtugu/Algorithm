import sys
input = sys.stdin.readline


def calc(string):
    temp = ''
    for a in string.split():
        temp += a

    result = 0
    numb = ''
    for a in reversed(temp):
        if a == '+':
            result += int(numb)
            numb = ''
        elif a == '-':
            result -= int(numb)
            numb = ''
        else:
            numb = a + numb
    result += int(numb)

    if not result: return True
    return False


def go(cnt, N, string):
    if cnt == N:
        if calc(string): print(string)
        return
    
    for a in [' ', '+', '-']:
        go(cnt+1, N, string+a+str(cnt+1))


T = int(input())

for _ in range(T):
    N = int(input())
    go(1, N, '1')
    print()
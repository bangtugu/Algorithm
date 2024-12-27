import sys
input = sys.stdin.readline

N = int(input())


def check(n):
    for i in range(2, int(n**(1/2))+1):
        if not n%i: return False    
    return True


def dfs(n):
    if not check(n):
        return

    if n >= 10**(N-1):
        print(n)
        return

    for i in range(1, 10, 2):
        if check(10*n + i):
            dfs(10*n + i)


for i in range(2, 10):
    dfs(i)
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
blue = list(map(int, input().split()))
red = list(map(int, input().split()))
target = [i for i in range(M)]
blue.sort()


def check(n):
    if target[n] != n:
        target[n] = check(target[n])
    return target[n]


def set_target(n):
    if n+1 >= M: return
    t = check(n+1)
    target[n] = t


def binary(n):
    s, e = 0, len(blue)-1

    can = len(blue)-1
    while s < e:
        m = (s+e)//2
        if blue[m] <= n:
            s = m+1
        else:
            can = m
            e = m
    return can


for i in range(K):
    temp = binary(red[i])
    temp = check(temp)
    print(blue[temp])
    set_target(temp)
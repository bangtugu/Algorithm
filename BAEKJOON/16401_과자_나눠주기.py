import sys
input = sys.stdin.readline

M, N = map(int, input().split())
lst = list(map(int, input().split()))
s, e = 1, max(lst)


def check(l):
    cnt = 0
    for stick in lst:
        cnt += stick//l
    
    if cnt >= M: return True
    return False


answer = 0
while s <= e:

    m = (s+e)//2

    if check(m):
        answer = max(answer, m)
        s = m + 1
    else:
        e = m - 1

print(answer)
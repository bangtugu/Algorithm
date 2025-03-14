import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))


def get(n):
    s, e = 0, len(answer)-1
    while s <= e:
        m = (s+e)//2

        if answer[m] == n: return m
        elif answer[m] > n:
            e = m - 1
        else:
            s = m + 1
    
    return s


answer = [lst[0]]
for n in lst:
    if n > answer[-1]:
        answer.append(n)
    else:
        idx = get(n)
        answer[idx] = n

print(len(answer))
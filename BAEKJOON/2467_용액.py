import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
s, e = 0, N-1
answer = max(abs(lst[s]), lst[e])*2
answer_lst = [lst[s], lst[e]]

while s < e:
    now = lst[s]+lst[e]

    if abs(now) < abs(answer):
        answer = now
        answer_lst = [lst[s], lst[e]]

    if now == 0:
        break
    
    if abs(lst[s+1]+lst[e]) < abs(lst[s]+lst[e-1]):
        s += 1
    else:
        e -= 1

print(*answer_lst)

'''

5
-99 -2 -1 4 98

'''
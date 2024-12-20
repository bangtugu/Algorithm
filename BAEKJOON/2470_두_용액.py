import sys
input = sys.stdin.readline

N = int(input())
lst = sorted(list(map(int, input().split())))

s, e = 0, N-1
temp = lst[s]+lst[e]
answer = [lst[s], lst[e]]
while s < e:
    now = lst[s]+lst[e]

    if abs(now) < abs(temp):
        answer = [lst[s], lst[e]]
        temp = now
    
    if now == 0:
        answer = [lst[s], lst[e]]
        break
    if lst[s]+lst[e] > 0:
        e -= 1
    else:
        s += 1

print(*answer)
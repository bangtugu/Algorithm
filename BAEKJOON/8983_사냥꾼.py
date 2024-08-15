import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
shooting_lange = sorted(list(map(int, input().split())))

answer = 0
for _ in range(N):
    x, y = map(int, input().split())
    if y > L: continue
    l, r = max(1, x-L+y), min(1000000000, x+L-y)
    s, e = 0, len(shooting_lange)-1

    while s <= e:
        m = (s+e)//2
        if l <= shooting_lange[m] <= r:
            answer += 1
            break
        elif shooting_lange[m] < l:
            s = m + 1
        else:
            e = m - 1

print(answer)
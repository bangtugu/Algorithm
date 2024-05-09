import sys
input = sys.stdin.readline


N, L = map(int, input().split())
ladder = [list(map(int, input().split())) for _ in range(N)]


def position(idx, time):
    
    l, d = ladder[idx]
    if l == L: return 0, L-1, d
    
    if time:
        cnt = time // (L-l)
        temp = time % (L-l)

        s = temp if (not d and not cnt) or (d and cnt) else L-l-temp
        e = temp + l if (not d and not cnt) or (d and cnt) else L-temp
        d = not d if cnt % 2 else d
    else:
        s = L-l if d else 0
        e = L if d else l

    return s, e, d


def uptime(now, next, time):
    s1, e1, d1 = now
    s2, e2, d2 = next

    if s1 <= s2 <= e1 or s1 <= e2 <= e1 or s2 <= s1 <= e2 or s2 <= e1 <= e2: 
        return time

    if d1 == d2:
        if d1:
            return time + min(s1, s2) + min(e1-s2, e2-s1)//2
        else:
            return time + (L-max(e1, e2)) + min(e1-s2, e2-s1)//2
    else:
        if (d1 and s1 > e2) or (d2 and s2 > e1):
            return time + max(s1-e2, s2-e1)//2
        else:
            return time + max(s2-e1, s1-e2)//2 + L-max(e1, e2) + min(s1, s2)


time = 0
for i in range(0, N-1):
    now = position(i, time)
    next = position(i+1, time)
    time = uptime(now, next, time)

print(time)
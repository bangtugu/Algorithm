import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lines = []
line_dic = {}
check = set(list(range(1, M+1)))
for i in range(1, M+1):
    a, b = map(int, input().split())
    if a < b:
        a += N
        b += N
    else:
        b += N
        lines.append([a, b, i])
        a += N
        b += N
    
    lines.append([a, b, i])

lines.sort(key = lambda x: (x[0], x[1]))

ps, pe, pline = 0, 0, 0
for i in range(len(lines)):
    if not pline:
        ps, pe, pline = lines[i]
        continue

    s, e, line = lines[i]
    if ps <= s and e <= pe:
        check.discard(line)
    else:
        if s <= ps and pe <= e:
            check.discard(pline)
        ps, pe, pline = lines[i]


print(*sorted(list(check)))
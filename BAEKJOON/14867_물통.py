import sys
input = sys.stdin.readline


a, b, c, d = input().split()

goal = c + ' ' + d

a, b, c, d = map(int, [a, b, c, d])

check = set(['0 0'])

lst = ['0 0', 'end']
idx = 0
answer = 0
while idx < len(lst):
    now = lst[idx]
    if now == 'end':
        idx += 1
        answer += 1
        lst.append('end')
        if lst[idx] == 'end':
            break
        continue

    if now == goal:
        break

    ba, bb = map(int, now.split())
    
    for aa, ab in [
        [a, bb],
        [ba, b],
        [0, bb],
        [ba, 0],
        [ba + bb, 0],
        [a, ba + bb - a],
        [0, ba + bb],
        [ba + bb - b, b]
    ]:
        if aa < 0 or aa > a or ab < 0 or ab > b: continue
        
        temp = str(aa) + ' ' + str(ab)
        if temp in check: continue
        
        check.add(temp)
        lst.append(temp)

    idx += 1

if lst[-1] == lst[-2]: print(-1)
else: print(answer)
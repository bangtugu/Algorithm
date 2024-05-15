import sys
input = sys.stdin.readline
# sys.setrecursionlimit(N) 재귀시 사용


'''
goal
1	2	3
4	5	6
7	8	

1 0 3
4 2 5
7 8 6

3 6 0
8 1 2
7 4 5

'''

goal = '123456780'
start = []
for _ in range(3):
    for num in input().split():
        start.append(num)

for i in range(9):
    if start[i] == '0':
        point = i


def lts(lst):
    string = ''
    for i in range(9):
        string += str(lst[i])
    return string


check = set([lts(start)])
answer = 0
idx = 0
dp = [-1, +1, -3, +3]
lst = [[start, point], ['end', 0]]
while idx < len(lst):
    now, point = lst[idx]

    if now == 'end':
        answer += 1
        idx += 1
        lst.append(['end', 0])
        continue

    if lts(now) == goal:
        break

    if point%3 != 0:
        temp = now[:]
        temp[point], temp[point-1] = temp[point-1], temp[point]
        string = lts(temp)
        if string not in check:
            check.add(string)
            lst.append([temp, point-1])
    if point%3 != 2:
        temp = now[:]
        temp[point], temp[point+1] = temp[point+1], temp[point]
        string = lts(temp)
        if string not in check:
            check.add(string)
        lst.append([temp, point+1])
    if point//3 != 0:
        temp = now[:]
        temp[point], temp[point-3] = temp[point-3], temp[point]
        string = lts(temp)
        if string not in check:
            check.add(string)
        lst.append([temp, point-3])
    if point//3 != 2:
        temp = now[:]
        temp[point], temp[point+3] = temp[point+3], temp[point]
        string = lts(temp)
        if string not in check:
            check.add(string)
        lst.append([temp, point+3])
    
    idx += 1
    if idx == 5: break


print(-1 if idx == len(lst) else answer)


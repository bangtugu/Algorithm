'''TC1'''
x = 10
y = 40
n = 5
result = 2
'''TC2'''
x = 10
y = 40
n = 30
result = 1
'''TC3'''
x = 2
y = 5
n = 4
result = -1


TC = 3
x = [10, 10, 2]
y = [40, 40, 5]
n = [5, 30, 4]
result = [2, 1, -1]


def solution(x, y, n):

    sett = set([x])
    lst = [[x, 0]]
    idx = 0
    while idx < len(lst):
        now, cnt = lst[idx]

        if now == y:
            return cnt
        
        next = [now*2, now*3, now+n]
        
        for i in range(3):
            if next[i] in sett: continue
            if next[i] > y: continue
            lst.append([next[i], cnt+1])
            sett.add(next[i])

        idx += 1

    return -1


for t in range(TC):
    answer = solution(x[t], y[t], n[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
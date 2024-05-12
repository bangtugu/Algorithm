'''TC1'''
n = 2
l = 4
r = 17
result = 8


TC = 2
n = [2, 2]
l = [4, 7]
r = [17, 10]
result = [8, 3]


def solution(n, l, r):

    answer = 0
    for i in range(l-1, r):
        
        while i >= 5:
            if i % 5 == 2: break
            i //= 5
        if i % 5 == 2: continue
        answer += 1

    return answer


for t in range(TC):
    answer = solution(n[t], l[t], r[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
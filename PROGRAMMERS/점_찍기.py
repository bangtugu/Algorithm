'''TC1'''
k = 2
d = 4
result = 6
'''TC2'''
k = 1
d = 5
result = 26


TC = 2
k = [2, 1]
d = [4, 5]
result = [6, 26]


def solution(k, d):
    
    answer = 0

    for i in range(0, d+1, k):
        answer += int((d**2-i**2)**(1/2))//k + 1

    return answer


for t in range(TC):
    answer = solution(k[t], d[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
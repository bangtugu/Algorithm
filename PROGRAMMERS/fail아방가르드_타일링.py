'''TC1'''
n = 2
result = 3
'''TC2'''
n = 3
result = 10


TC = 2
n = [2, 3]
result = [3, 10]


def solution(n):

    lst = [1, 3, 10, 2, 2, 4]

    '''코드 들어갈곳'''
    return


for t in range(TC):
    answer = solution(n[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
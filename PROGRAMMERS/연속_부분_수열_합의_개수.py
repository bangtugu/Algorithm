'''TC1'''
elements = [7,9,1,1,4]
result = 18


TC = 1
elements = [[7,9,1,1,4]]
result = [18]


def solution(elements):
    
    sett = set()
    N = len(elements)
    elements = elements*2

    for i in range(N):
        for j in range(1, N+1):
            sett.add(sum(elements[i:i+j]))

    return len(sett)


for t in range(TC):
    answer = solution(elements[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
'''TC1'''
r1 = 2
r2 = 3
result = 20


TC = 3
r1 = [2, 1, 25]
r2 = [3, 3, 39]
result = [20, 28, 2836]


def solution(r1, r2):
    answer = 0

    for x in range(1, r2+1):
        maxy = (r2*r2 - x*x)**0.5
        if x >= r1:
            answer += int(maxy)+1
        else:
            miny = (r1*r1 - x*x)**0.5
            answer += int(maxy) + 1
            if miny == int(miny):
                answer -= int(miny)
            else:
                answer -= int(miny) + 1

    return answer*4


for t in range(TC):
    answer = solution(r1[t], r2[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
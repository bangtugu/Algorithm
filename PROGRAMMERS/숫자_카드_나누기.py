'''TC1'''
arrayA = [10, 17]
arrayB = [5, 20]
result = 0
'''TC2'''
arrayA = [10, 20]
arrayB = [5, 17]
result = 10
'''TC3'''
arrayA = [14, 35, 119]
arrayB = [18, 30, 102]
result = 7


TC = 3
arrayA = [[10, 17], [10, 20], [14, 35, 119]]
arrayB = [[5, 20], [5, 17], [18, 30, 102]]
result = [0, 10, 7]


def solution(arrayA, arrayB):

    arrayA.sort()
    arrayB.sort()

    lstA = [arrayA[0]]
    lstB = [arrayB[0]]

    for i in range(2, arrayA[0]//2+1):
        if not arrayA[0] % i:
            if i in lstA: break
            lstA.extend([i, arrayA[0]//i])

    for i in range(2, arrayB[0]//2+1):
        if not arrayB[0] % i:
            if i in lstB: break
            lstB.extend([i, arrayB[0]//i])

    lstA.sort()
    lstB.sort()

    answerA = 0
    idx = len(lstA)-1
    while idx >= 0:
        now = lstA[idx]

        for num in arrayA:
            if num%now: break
        else:
            for num in arrayB:
                if not num%now: break
            else:
                answerA = now

        if answerA: break
        idx -= 1

    answerB = 0
    idx = len(lstB)-1
    while idx >= 0:
        now = lstB[idx]

        for num in arrayB:
            if num%now: break
        else:
            for num in arrayA:
                if not num%now: break
            else:
                answerB = now
        
        if answerB: break
        idx -= 1
    
    answer = max(answerA, answerB)

    return answer


for t in range(TC):
    answer = solution(arrayA[t], arrayB[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
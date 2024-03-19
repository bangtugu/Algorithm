'''TC1'''
beginning = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
target = [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
result = 5
'''TC2'''
beginning = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
target = [[1, 0, 1], [0, 0, 0], [0, 0, 0]]
result = -1


TC = 2
beginning = [[[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
target = [[[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]], [[1, 0, 1], [0, 0, 0], [0, 0, 0]]]
result = [5, -1]


def solution(beginning, target):
    
    N = len(beginning)
    M = len(beginning[0])

    different = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if beginning[i][j] != target[i][j]:
                different[i][j] = 1
    
    answer = 0
    for j in range(M):
        if different[0][j]:
            answer += 1
            for i in range(N):
                different[i][j] = 0 if different[i][j] else 1
    
    for i in range(N):
        v = sum(different[i])
        if v == M:
            answer += 1
        elif v:
            return -1
    
    return min(M+N-answer, answer)


for t in range(TC):
    answer = solution(beginning[t], target[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
'''TC1'''
triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
result = 30


TC = 1
triangle = [[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]]
result = [30]


def solution(triangle):
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]


for t in range(TC):
    answer = solution(triangle[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
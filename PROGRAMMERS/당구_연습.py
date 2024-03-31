'''TC1'''
m = 10
n = 10
startX = 3
startY = 7
balls = [[7, 7], [2, 7], [7, 3]]
result = [52, 37, 116]


TC = 1
m = [10]
n = [10]
startX = [3]
startY = [7]
balls = [[[7, 7], [2, 7], [7, 3]]]
result = [[52, 37, 116]]


def solution(m, n, startX, startY, balls):


    def calc(y1, x1, y2, x2):
        yy = abs(y1-y2)
        xx = abs(x1-x2)

        return yy**2+xx**2


    answer = []    
    for X, Y in balls:
        min_v = max(n, m)**3

        if not (startX == X and startY > Y):
            min_v = min(min_v, calc(startY, startX, -Y, X))
        if not (startX == X and startY < Y):
            min_v = min(min_v, calc(startY, startX, 2*n-Y, X))
        if not (startY == Y and startX > X):
            min_v = min(min_v, calc(startY, startX, Y, -X))
        if not (startY == Y and startX < X):
            min_v = min(min_v, calc(startY, startX, Y, 2*m-X))

        answer.append(min_v)

    return answer


for t in range(TC):
    answer = solution(m[t], n[t], startX[t], startY[t], balls[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
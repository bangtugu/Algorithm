'''TC1'''
e = 8
starts = [1,3,7]
result = [6,6,8]


TC = 1
e = [8]
starts = [[1,3,7]]
result = [[6,6,8]]


def solution(e, starts):

    count = [0] * (e+1)

    for i in range(2, e+1):
        for j in range(0, e+1, i):
            count[j] += 2

    dp = [0] * (e+1)
    max_v = 0
    max_idx = e
    for i in range(e, 0, -1):
        if count[i]>= max_v:
            max_v = count[i]
            max_idx = i
        dp[i] = max_idx

    answer = [dp[s] for s in starts]

    return answer


for t in range(TC):
    answer = solution(e[t], starts[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
'''TC1'''
sequence = [2, 3, -6, 1, 3, -1, 2, 4]
result = 10


TC = 1
sequence = [[2, 3, -6, 1, 3, -1, 2, 4]]
result = [10]


def solution(sequence):

    lst = [sequence[0]] + [0] * (len(sequence)-1)

    for i in range(1, len(sequence)):
        if i%2:
            lst[i] = lst[i-1] - sequence[i]
        else:
            lst[i] = lst[i-1] + sequence[i]

    maxv = max(lst)
    minv = min(lst)
    return max(abs(maxv), abs(minv), abs(maxv-minv))


for t in range(TC):
    answer = solution(sequence[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
'''TC1'''
sequence = [1, 2, 3, 4, 5]
k = 7
result = [2, 3]
'''TC2'''
sequence = [1, 1, 1, 2, 3, 4, 5]
k = 5
result = [6, 6]
'''TC3'''
sequence = [2, 2, 2, 2, 2]
k = 6
result = [0, 2]


TC = 3
sequence = [[1, 2, 3, 4, 5], [1, 1, 1, 2, 3, 4, 5], [2, 2, 2, 2, 2]]
k = [7, 5, 6]
result = [[2, 3], [6, 6], [0, 2]]


def solution(sequence, k):
    
    answer = [0, len(sequence)]
    idx1 = 0
    idx2 = -1
    now_sum = 0
    while idx2 < len(sequence):
        
        if now_sum < k and idx2+1 < len(sequence):
            idx2 += 1
            now_sum += sequence[idx2]
        elif idx1 < len(sequence):
            now_sum -= sequence[idx1]
            idx1 += 1
        else:
            break
        
        if now_sum == k:
            if idx2 - idx1 < answer[1] - answer[0]:
                answer = [idx1, idx2]

    return answer


for t in range(TC):
    answer = solution(sequence[t], k[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
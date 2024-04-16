'''TC1'''
numbers = [2, 3, 3, 5]
result = [3, 5, 5, -1]
'''TC2'''
numbers = [9, 1, 5, 3, 6, 2]
result = [-1, 5, 6, 6, -1, -1]


TC = 2
numbers = [[2, 3, 3, 5], [9, 1, 5, 3, 6, 2]]
result = [[3, 5, 5, -1], [-1, 5, 6, 6, -1, -1]]


def solution(numbers):

    answer = [-1] * len(numbers)

    now_max = numbers[-1]
    max_idx = len(numbers)-1
    for i in range(len(numbers)-2, -1, -1):
        if numbers[i] >= now_max: 
            now_max = numbers[i]
            max_idx = i
            continue

        for j in range(i+1, max_idx+1):
            if numbers[j] == numbers[i]:
                answer[i] = answer[j]
                break
            if numbers[j] > numbers[i]:
                answer[i] = numbers[j]
                break
            if answer[j] > numbers[i]:
                answer[i] = answer[j]
                break
    
    return answer


for t in range(TC):
    answer = solution(numbers[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
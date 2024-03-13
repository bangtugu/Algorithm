'''TC1'''
bandage = [5, 1, 5]
health = 30
attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]
result = 5
'''TC2'''
bandage = [3, 2, 7]
health = 20
attacks = [[1, 15], [5, 16], [8, 6]]
result = -1
'''TC3'''
bandage = [4, 2, 7]
health = 20
attacks = [[1, 15], [5, 16], [8, 6]]
result = -1
'''TC4'''
bandage = [1, 1, 1]
health = 5
attacks = [[1, 2], [3, 2]]
result = 3


TC = 4
bandage = [[5, 1, 5], [3, 2, 7], [4, 2, 7], [1, 1, 1]]
health = [30, 20, 20, 5]
attacks = [[[2, 10], [9, 15], [10, 5], [11, 5]], [[1, 15], [5, 16], [8, 6]], [[1, 15], [5, 16], [8, 6]], [[1, 2], [3, 2]]]
result = [5, -1, -1, 3]


def solution(bandage, health, attacks):
    answer = health

    att = [0] * attacks[-1][0]
    for t, d in attacks:
        att[t-1] = d
    
    cont = 0
    for i in range(len(att)):
        if att[i]:
            cont = 0
            answer -= att[i]
            if answer <= 0 : return -1
        else:
            answer += bandage[1]
            cont += 1
            if cont >= bandage[0]:
                answer += bandage[2]
                cont = 0
            answer = min(answer, health)
    
    return answer


for t in range(TC):
    answer = solution(bandage[t], health[t], attacks[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, correct, comment))
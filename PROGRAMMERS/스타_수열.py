'''TC1'''
a = [0]
result = 0
'''TC2'''
a = [5,2,3,3,5,3]
result = 4
'''TC3'''
a = [0,3,3,0,7,2,0,2,2,0]
result = 8


TC = 3
a = [[0], [5,2,3,3,5,3], [0,3,3,0,7,2,0,2,2,0]]
result = [0, 4, 8]


def solution(a):
    cross_dic = {}
    left = 1
    right = 2

    for i in range(len(a)):
        if a[i] not in cross_dic.keys():
            cross_dic[a[i]] = [0, 0, 0]
        
        if i > 0 and a[i] != a[i-1] and not (cross_dic[a[i]][0] == right and i-2 == cross_dic[a[i]][2]):
            cross_dic[a[i]][0] = left
            cross_dic[a[i]][1] += 1
            cross_dic[a[i]][2] = i
        elif i+1 < len(a) and a[i] != a[i+1]:
            cross_dic[a[i]][0] = right
            cross_dic[a[i]][1] += 1
            cross_dic[a[i]][2] = i

    answer = 0
    for i in cross_dic.keys():
        answer = max(answer, cross_dic[i][1])

    return answer * 2


for t in range(TC):
    answer = solution(a[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
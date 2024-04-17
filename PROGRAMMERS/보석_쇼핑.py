'''TC1'''
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
result = [3, 7]
'''TC2'''
gems = ["AA", "AB", "AC", "AA", "AC"]
result = [1, 3]
'''TC3'''
gems = ["XYZ", "XYZ", "XYZ"]
result = [1, 1]
'''TC4'''
gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
result = [1, 5]


TC = 4
gems = [["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"], ["AA", "AB", "AC", "AA", "AC"], ["XYZ", "XYZ", "XYZ"], ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]]
result = [[3, 7], [1, 3], [1, 1], [1, 5]]


def solution(gems):

    lst = list(set(gems))
    dic = {}
    for i in range(len(lst)):
        dic[lst[i]] = i
    cnt = [0]*len(lst)

    s, e, buy = 0, -1, False
    answer = [1, len(gems)]

    while s < len(gems):

        if buy:

            if e-s < answer[1]-answer[0]:
                answer = [s+1, e+1]

            idx = dic[gems[s]]
            cnt[idx] -= 1
            if cnt[idx] == 0: buy = False
            s += 1
            
        else:
            e += 1
            if e >= len(gems): break
            idx = dic[gems[e]]
            cnt[idx] += 1
            if 0 not in cnt: buy = True
    
    return answer


for t in range(TC):
    answer = solution(gems[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
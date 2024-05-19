'''TC1'''
k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
result = 3
'''TC2'''
k = 4
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
result = 2
'''TC3'''
k = 2
tangerine = [1, 1, 1, 1, 2, 2, 2, 3]
result = 1


TC = 3
k = [6, 4, 2]
tangerine = [[1, 3, 2, 5, 4, 5, 2, 3], [1, 3, 2, 5, 4, 5, 2, 3], [1, 1, 1, 1, 2, 2, 2, 3]]
result = [3, 2, 1]


def solution(k, tangerine):
    
    t_dic = {}
    for s in tangerine:
        if s in t_dic.keys(): t_dic[s] += 1 
        else: t_dic[s] = 1
    
    lst = [t_dic[i] for i in t_dic.keys()]
    lst.sort(reverse = True)

    answer = 0
    for cnt in lst:
        k -= cnt
        answer += 1
        if k <= 0: break
    
    return answer


for t in range(TC):
    answer = solution(k[t], tangerine[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
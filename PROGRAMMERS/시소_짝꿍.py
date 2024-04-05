'''TC1'''
weights = [100,180,360,100,270]
result = 4


TC = 1
weights = [[100,180,360,100,270]]
result = [4]


def solution(weights):
    w_dic = {}
    
    for w in weights:
        if w in w_dic.keys():
            w_dic[w] += 1
        else:
            w_dic[w] = 1
    
    w_set = set(w_dic.keys())
    w_lst = list(w_set)
    w_lst.sort()
    
    answer = 0
    for w in w_lst:
        for p in w_lst:
            if w == p:
                answer += w_dic[w] * (w_dic[w]-1)//2
            elif w*4 == p*3:
                answer += w_dic[w] * w_dic[p]
            elif w*2 == p:
                answer += w_dic[w] * w_dic[p]
            elif w*3 == p*2:
                answer += w_dic[w] * w_dic[p]
        
    return answer


for t in range(TC):
    answer = solution(weights[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
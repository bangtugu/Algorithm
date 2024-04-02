'''TC1'''
picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
result = 12
'''TC2'''
picks = [0, 1, 1]
minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
result = 50


TC = 2
picks = [[1, 3, 2], [0, 1, 1]]
minerals = [["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]]
result = [12, 50]


def solution(picks, minerals):
    pm = [[1] * len(minerals), [1] * len(minerals), [1] * len(minerals)]
    
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            pm[1][i] = 5
            pm[2][i] = 25
        elif minerals[i] == 'iron':
            pm[2][i] = 5
    
    N = sum(picks)*5
    if sum(picks)*5 > len(minerals):
        N = len(minerals)
    
    answer = [len(minerals)*25]
    
    
    def pick(lst):
        if len(lst)*5 >= N:
            temp = 0
            for i in range(N):
                temp += pm[lst[i//5]][i]
            answer[0] = min(answer[0], temp)
            return
            
        else:
            for i in range(3):
                if picks[i] == 0: continue
                picks[i] -= 1
                pick(lst+[i])
                picks[i] += 1
        
    
    pick([])
    
    return answer[0]

for t in range(TC):
    answer = solution(picks[t], minerals[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
'''TC1'''
storey = 16
result = 6
'''TC2'''
storey = 2554
result = 16


TC = 3
storey = [16, 2554, 555555]
result = [6, 16, 26]


def solution(storey):
    storey = str(storey)
    lst = []
    for i in range(len(storey)-1, -1, -1):
        lst.append(int(storey[i]))
    
    idx = 0
    answer = 0
    while idx < len(lst):

        if lst[idx] < 5:
            answer += lst[idx]
        elif lst[idx] > 5:
            if idx == len(lst)-1: lst.append(0)
            answer += 10 - lst[idx]
            lst[idx+1] += 1
        
        else:
            if idx == len(lst)-1:
                answer += 5
            else:
                if lst[idx+1] < 5:
                    answer += 5
                else:
                    answer += 10 - lst[idx]
                    lst[idx+1] += 1
        
        idx += 1

    return answer


for t in range(TC):
    answer = solution(storey[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
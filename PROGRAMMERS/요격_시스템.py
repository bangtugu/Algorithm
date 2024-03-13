'''TC1'''
targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
result = 3


TC = 1
targets = [[[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]]
result = [3]


def solution(targets):
    
    targets.sort(key = lambda  x : x[0])

    answer = 1
    s, e = targets[0]
    for i in range(1, len(targets)):
        
        ns, ne = targets[i]
        if ns >= e:
            s = ns
            e = ne
            answer += 1
            continue
        if ne < e:
            e = ne
        if ns > s:
            s = ns

    return answer


for t in range(TC):
    answer = solution(targets[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
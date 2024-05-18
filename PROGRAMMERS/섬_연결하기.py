'''TC1'''
n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
result = 4


TC = 1
n = [4]
costs = [[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]]
result = [4]


def solution(n, costs):
    
    costs.sort(key = lambda x: x[2])
    table = [set([i]) for i in range(n)]

    answer = 0
    for s, e, c in costs:
        if s in table[e]: continue
        answer += c
        lst1 = list(table[s])
        lst2 = list(table[e])
        for i in lst1:
            for j in lst2:
                table[i].add(j)
                table[j].add(i)
        if len(table[s]) == n: break

    return answer


for t in range(TC):
    answer = solution(n[t], costs[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
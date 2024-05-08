'''TC1'''
routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
result = 2


TC = 1
routes = [[[-20,-15], [-14,-5], [-18,-13], [-5,-3]]]
result = [2]


def solution(routes):
    
    answer = 1
    routes.sort(key = lambda x: x[0])
    e = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] > e:
            answer += 1
            e = routes[i][1]
        else:
            e = min(e, routes[i][1])

    return answer


for t in range(TC):
    answer = solution(routes[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
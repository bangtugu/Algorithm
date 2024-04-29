'''TC1'''
n = 9
path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[8,5],[6,7],[4,1]]
result = True
'''TC2'''
n = 9
path = [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]]
order = [[4,1],[5,2]]
result = True
'''TC3'''
n = 9
path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[4,1],[8,7],[6,5]]
result = False


TC = 3
n = [9, 9, 9]
path = [[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]]
order = [[[8,5],[6,7],[4,1]], [[4,1],[5,2]], [[4,1],[8,7],[6,5]]]
result = [True, True, False]


def solution(n, path, order):
    
    # table = [[] for _ in range(n)]
    top = [-1]*n
    for a, b in path:
        top[b] = a

    b_set = set()
    a_set = set()
    for before, after in order:
        b_set.add(before)
        a_set.add(after)

    
    


    return True


for t in range(TC):
    answer = solution(n[t], path[t], order[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
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
    
    table = [[] for _ in range(n)]
    for a, b in path:
        table[a].append(b)
        table[b].append(a)

    top = [-2]*n
    top[0] = -1
    idx = 0
    lst = [0]
    while idx < len(lst):
        now = lst[idx]
        for next in table[now]:
            if top[next] != -2: continue
            top[next] = now
            lst.append(next)
        idx += 1

    b_dic = {}
    b_set = set()
    a_dic = {}
    a_set = set()
    for before, after in order:
        b_set.add(before)
        a_set.add(after)
        b_dic[after] = before
        a_dic[before] = after
    if 0 in a_set: return False


    import sys
    sys.setrecursionlimit(200000)


    def path_finding(s, never):
        print(never)
        path = [s]
        now = s
        while True:
            now = top[now]
            if now == -1:
                for p in path:
                    top[p] = -1
                return True

            if now in never: return False
            if now in b_set: never.add(a_dic[now])
            if now in a_set: 
                never.add(now)
                if not path_finding(b_dic[now], never): return False
                never.remove(now)
            if now in b_set: never.remove(a_dic[now])

            path.append(now)


    for b in list(b_set):
        if not path_finding(b, set([a_dic[b]])): return False

    return True


for t in range(TC):
    answer = solution(n[t], path[t], order[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
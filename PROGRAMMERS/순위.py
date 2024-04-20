'''TC1'''
n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
result = 2


TC = 1
n = [5]
results = [[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]]
result = [2]


def find_case(n, table, w_lst, l_lst):
    change = False

    for i in range(n):
        if len(w_lst[i]) + len(l_lst[i]) == n-1: continue

        for loser in list(w_lst[i]):
            for lloser in w_lst[loser]:
                if table[i][lloser]: continue
                table[i][lloser] = 1
                w_lst[i].add(lloser)
                l_lst[lloser].add(i)
                change = True 

        for winner in list(l_lst[i]):
            for wwinner in l_lst[winner]:
                if table[i][wwinner]: continue
                table[i][wwinner] = 1
                l_lst[i].add(wwinner)
                w_lst[wwinner].add(i)
                change = True

    return change, table, w_lst, l_lst


def get_rank(n, lst1, lst2):
    
    rank = [0]*n
    for i in range(n):
        if len(lst1[i]) + len(lst2[i]) == n-1:
            rank[i] = 1+len(lst2[i])

    return rank


def solution(n, results):
    
    table = [[0]*n for _ in range(n)]
    w_lst = [set() for _ in range(n)]
    l_lst = [set() for _ in range(n)]

    for w, l in results:
        table[w-1][l-1] = 1
        w_lst[w-1].add(l-1)
        l_lst[l-1].add(w-1)

    change = True
    while change:
        change, table, w_lst, l_lst = find_case(n, table, w_lst, l_lst)

    rank = get_rank(n, w_lst, l_lst)

    return n - rank.count(0)


for t in range(TC):
    answer = solution(n[t], results[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
'''TC1'''
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
result = 2
'''TC2'''
n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
result = 1


TC = 2
n = [3, 3]
computers = [[[1, 1, 0], [1, 1, 0], [0, 0, 1]], [[1, 1, 0], [1, 1, 1], [0, 1, 1]]]
result = [2, 1]


def solution(n, computers):
    
    check = [0]*n
    cnt = 0
    for i in range(n):
        if check[i]: continue
        cnt += 1
        idx = 0
        lst = [i]
        while idx < len(lst):
            now = lst[idx]
            for j in range(n):
                if check[j]: continue
                if computers[now][j]:
                    lst.append(j)
                    check[j] = cnt
            idx += 1

    return cnt


for t in range(TC):
    answer = solution(n[t], computers[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
'''TC1'''
m = 4
n = 3
puddles = [[2, 2]]
result = 4


TC = 1
m = [4]
n = [3]
puddles = [[[2, 2]]]
result = [4]


def solution(m, n, puddles):
    
    table = [[0]*m for _ in range(n)]
    check = [[0]*m for _ in range(n)]
    table[0][0] = 1

    for x, y in puddles:
        check[y-1][x-1] = 1
    
    lst = [[0, 0]]
    idx = 0
    while idx < len(lst):
    
        y, x = lst[idx]
        if x > 0: table[y][x] += table[y][x-1]
        if y > 0: table[y][x] += table[y-1][x]

        if y < n-1 and table[y+1][x] != -1 and not check[y+1][x]:
            check[y+1][x] = 1
            lst.append([y+1, x])

        if x < m-1 and table[y][x+1] != -1 and not check[y][x+1]:
            check[y][x+1] = 1
            lst.append([y, x+1])

        idx += 1

    return table[n-1][m-1] % 1000000007


for t in range(TC):
    answer = solution(m[t], n[t], puddles[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
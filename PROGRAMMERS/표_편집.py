'''TC1'''
n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
result = "OOOOXOOO"
'''TC2'''
n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
result = "OOXOXOOO"


TC = 2
n = [8, 8]
k = [2, 2]
cmd = [["D 2","C","U 3","C","D 4","C","U 2","Z","Z"], ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]]
result = ["OOOOXOOO", "OOXOXOOO"]


def solution(n, k, cmd):
    lst = [[True, i-1, i+1] for i in range(n)]
    lst[0][1] = lst[-1][2] = None
    idx = k
    temp = []
    for line in cmd:
        if line[0] == 'D':
            for i in range(int(line[2:])):
                idx = lst[idx][2]
        elif line[0] == 'U':
            for i in range(int(line[2:])):
                idx = lst[idx][1]

        elif line[0] == 'C':
            lst[idx][0] = False
            temp.append(idx)

            up, down = lst[idx][1], lst[idx][2]
            if up or up == 0:
                lst[up][2] = down
            if down:
                lst[down][1] = up
                idx = down
            else:
                idx = up

        else:
            i = temp.pop()
            lst[i][0] = True
            up, down = lst[i][1], lst[i][2]
            if up: lst[up][2] = i
            if down: lst[down][1] = i

    answer = ''
    for i in range(n):
        answer += 'O' if lst[i][0] else 'X'
    return answer


for t in range(TC):
    answer = solution(n[t], k[t], cmd[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
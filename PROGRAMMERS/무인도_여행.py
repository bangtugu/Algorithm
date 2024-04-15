'''TC1'''
maps = ["X591X","X1X5X","X231X", "1XXX1"]
result = [1, 1, 27]
'''TC2'''
maps = ["XXX","XXX","XXX"]
result = [-1]


TC = 2
maps = [["X591X","X1X5X","X231X", "1XXX1"], ["XXX","XXX","XXX"]]
result = [[1, 1, 27], [-1]]


def solution(maps):
    
    N = len(maps)
    M = len(maps[0])
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    check = [[0]*M for _ in range(N)]
    answer = []

    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'X':
                check[i][j] = 1
            elif not check[i][j]:
                
                idx = 0
                lst = [[i, j]]
                check[i][j] = 1
                food = int(maps[i][j])
                while idx < len(lst):
                    y, x = lst[idx]

                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]

                        if ny < 0 or ny >= N or nx < 0 or nx >= M or maps[ny][nx] == 'X' or check[ny][nx]: continue
                        check[ny][nx] = 1
                        food += int(maps[ny][nx])
                        lst.append([ny, nx])

                    idx += 1

                answer.append(food)

    return sorted(answer) if answer else [-1]


for t in range(TC):
    answer = solution(maps[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
'''TC1'''
maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
result = 16
'''TC2'''
maps = ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]
result = -1


TC = 2
maps = [["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"], ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]]
result = [16, -1]


def solution(maps):

    N = len(maps)
    M = len(maps[0])

    S = [0, 0]
    E = [0, 0]
    L = [0, 0]

    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                S = [i, j]
            elif maps[i][j] == 'E':
                E = [i, j]
            elif maps[i][j] == 'L':
                L = [i, j]

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    Lcheck = [[-1]*M for _ in range(N)]
    Echeck = [[-1]*M for _ in range(N)]

    Lcheck[S[0]][S[1]] = 0
    Echeck[L[0]][L[1]] = 0

    Llst = [S]
    idx = 0
    while idx < len(Llst):
        y, x = Llst[idx]

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or ny >= N or nx < 0 or nx >= M or maps[ny][nx] == 'X' or Lcheck[ny][nx] != -1: continue
            Lcheck[ny][nx] = Lcheck[y][x]+1
            Llst.append([ny, nx])

        idx += 1

    Elst = [L]
    idx = 0
    while idx < len(Elst):
        y, x = Elst[idx]

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or ny >= N or nx < 0 or nx >= M or maps[ny][nx] == 'X' or Echeck[ny][nx] != -1: continue
            Echeck[ny][nx] = Echeck[y][x]+1
            Elst.append([ny, nx])

        idx += 1
    
    print(Lcheck)
    print(Echeck)

    StL = Lcheck[L[0]][L[1]]
    LtE = Echeck[E[0]][E[1]]

    return Lcheck[L[0]][L[1]] + Echeck[E[0]][E[1]] if StL != -1 and LtE != -1 else -1


for t in range(TC):
    answer = solution(maps[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
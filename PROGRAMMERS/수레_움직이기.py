'''TC1'''
maze = [[1, 4], [0, 0], [2, 3]]
result = 3
'''TC2'''
maze = [[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]]
result = 7
'''TC3'''
maze = [[1, 5], [2, 5], [4, 5], [3, 5]]
result = 0
'''TC4'''
maze = [[4, 1, 2, 3]]
result = 0


TC = 4
maze = [[[1, 4], [0, 0], [2, 3]], [[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]], [[1, 5], [2, 5], [4, 5], [3, 5]], [[4, 1, 2, 3]]]
result = [3, 7, 0, 0]


def solution(maze):
    N, M = len(maze), len(maze[0])
    '''
    0	빈칸
    1	빨간 수레의 시작 칸
    2	파란 수레의 시작 칸
    3	빨간 수레의 도착 칸
    4	파란 수레의 도착 칸
    5	벽
    '''

    ry = rx = by = bx = rey = rex = bey = bex = 0
    red_check = [[0]*M for _ in range(N)]
    blue_check = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if maze[i][j] == 1:
                ry, rx = i, j
            elif maze[i][j] == 2:
                by, bx = i, j
            elif maze[i][j] == 3:
                rey, rex = i, j
            elif maze[i][j] == 4:
                bey, bex = i, j

    red_check[ry][rx] = 1
    blue_check[by][bx] = 1

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]


    def path_finder(ry, rx, by, bx, n, m):

        rf = bf = False
        if ry == rey and rx == rex: rf = True
        if by == bey and bx == bex: bf = True
        if rf and bf: return n

        red_possible = []
        blue_possible = []
        for i in range(4):
            if not rf:        
                nry = ry + dy[i]
                nrx = rx + dx[i]
                if nry < 0 or nry >= N or nrx < 0 or nrx >= M: continue
                if red_check[nry][nrx]: continue
                if maze[nry][nrx] == 5: continue

                red_possible.append([nry, nrx])

        for i in range(4):
            if not bf:
                nby = by + dy[i]
                nbx = bx + dx[i]
                if nby < 0 or nby >= N or nbx < 0 or nbx >= M: continue
                if blue_check[nby][nbx]: continue
                if maze[nby][nbx] == 5: continue

                blue_possible.append([nby, nbx])
        
        if (not rf and not red_possible) or (not bf and not blue_possible):
            return m

        if not rf and not bf:
            for nry, nrx in red_possible:
                for nby, nbx in blue_possible:
                    if nry == nby and nrx == nbx: continue
                    if nry == by and nrx == bx and nby == ry and nbx == rx: continue

                    red_check[nry][nrx] = n+2
                    blue_check[nby][nbx] = n+2
                    m = min(path_finder(nry, nrx, nby, nbx, n+1, m), m)
                    red_check[nry][nrx] = 0
                    blue_check[nby][nbx] = 0

        elif not rf:
            for nry, nrx in red_possible:
                if nry == by and nrx == bx: continue
                
                red_check[nry][nrx] = n+2
                m = min(path_finder(nry, nrx, by, bx, n+1, m), m)
                red_check[nry][nrx] = 0
                
        else:
            for nby, nbx in blue_possible:
                if nby == ry and nbx == rx: continue

                blue_check[nby][nbx] = n+2
                m = min(path_finder(ry, rx, nby, nbx, n+1, m), m)
                blue_check[nby][nbx] = 0

        return m
    

    answer = path_finder(ry, rx, by, bx, 0, 50)
    if answer == 50:
        return 0
    return answer


for t in range(TC):
    answer = solution(maze[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
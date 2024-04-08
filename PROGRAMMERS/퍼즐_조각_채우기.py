'''TC1'''
game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
result = 14
'''TC2'''
game_board = [[0,0,0],[1,1,0],[1,1,1]]
table = [[1,1,1],[1,0,0],[0,0,0]]
result = 0


TC = 2
game_board = [[[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[0,0,0],[1,1,0],[1,1,1]]]
table = [[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]], [[1,1,1],[1,0,0],[0,0,0]]]
result = [14, 0]


def solution(game_board, table):

    N = len(game_board)
    
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 1:
                game_board[i][j] = -1
            if table[i][j] == 0:
                table[i][j] = -1
            elif table[i][j] == 1:
                table[i][j] = 0

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    blank_cnt = 0
    block_cnt = 0
    blank_lst = []
    block_lst = []
    for i in range(N):
        for j in range(N):
            if not game_board[i][j]:
                blank_cnt += 1
                game_board[i][j] = blank_cnt
                lst = [[i, j]]
                idx = 0
                while idx < len(lst):
                    y, x = lst[idx]
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]

                        if nx < 0 or nx >= N or ny < 0 or ny >= N or game_board[ny][nx]: continue
                        game_board[ny][nx] = blank_cnt
                        lst.append([ny, nx])

                    idx += 1
                blank_lst.append(lst)

            if not table[i][j]:
                block_cnt += 1
                table[i][j] = block_cnt
                lst = [[i, j]]
                idx = 0
                while idx < len(lst):
                    y, x = lst[idx]
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]

                        if nx < 0 or nx >= N or ny < 0 or ny >= N or table[ny][nx]: continue
                        table[ny][nx] = block_cnt
                        lst.append([ny, nx])
                    
                    idx += 1
                block_lst.append(lst)

    
    def rotate(lst):
        miny, minx, maxy, maxx = 0, 0, 0, 0

        for y, x in lst:
            miny = min(y, miny)
            minx = min(x, minx)
            maxy = max(y, maxy)
            maxx = max(x, maxx)

        return


    for i in range(len(blank_lst)):
        n = len(lst)
        if n in blank_dic.keys():
            blank_dic[n].append(rotate(lst))
        else:
            blank_dic[n] = [rotate(lst)]
        blank_lst[i] = [n, y, x, lst]

    for lst in block_lst:
        n = len(lst)
        if n in block_dic.keys():
            block_dic[n].append(rotate(lst))
        else:
            block_dic[n] = [rotate(lst)]

    answer = 0


    return


for t in range(TC):
    answer = solution(game_board[t], table[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
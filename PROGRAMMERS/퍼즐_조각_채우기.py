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
    print(game_board)
    print(table)
    N = len(game_board)
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    blank_cnt = 2
    block_cnt = 2
    for i in range(N):
        for j in range(N):
            if not game_board[i][j]:
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
                
                blank_cnt += 1

            if table[i][j] == 1:
                table[i][j] = block_cnt
                lst = [[i, j]]
                idx = 0
                while idx < len(lst):
                    y, x = lst[idx]
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]

                        if nx < 0 or nx >= N or ny < 0 or ny >= N or table[ny][nx] != 1: continue
                        table[ny][nx] = block_cnt
                        lst.append([ny, nx])
                    
                    idx += 1
                
                block_cnt += 1


    print(game_board)
    print(table)


    return


for t in range(TC):
    answer = solution(game_board[t], table[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
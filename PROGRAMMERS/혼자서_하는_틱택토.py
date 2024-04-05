'''TC1'''
board = ["O.X", ".O.", "..X"]
result = 1
'''TC2'''
board = ["OOO", "...", "XXX"]
result = 0
'''TC3'''
board = ["...", ".X.", "..."]
result = 0
'''TC4'''
board = ["...", "...", "..."]
result = 1


TC = 4
board = [["O.X", ".O.", "..X"], ["OOO", "...", "XXX"], ["...", ".X.", "..."], ["...", "...", "..."]]
result = [1, 0, 0, 1]


def solution(board):
    
    O_check = False
    X_check = False

    for i in range(3):
        
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'O': O_check = True
            elif board[i][0] == 'X': X_check = True

        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'O': O_check = True
            elif board[0][i] == 'X': X_check = True

    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] == 'O': O_check = True
        elif board[1][1] == 'X': X_check = True

    if O_check and X_check: return 0

    O_cnt = 0
    X_cnt = 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                O_cnt += 1
            elif board[i][j] == 'X':
                X_cnt += 1
    
    if X_cnt > O_cnt or O_cnt >= X_cnt + 2: return 0

    if X_check and X_cnt != O_cnt: return 0

    if O_check and X_cnt == O_cnt: return 0

    return 1


for t in range(TC):
    answer = solution(board[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
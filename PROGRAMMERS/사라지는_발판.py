board, aloc, bloc, result = [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2], 5
# board, aloc, bloc, result = [[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2], 4
# board, aloc, bloc, result = [[1, 1, 1, 1, 1]], [0, 0], [0, 4], 4
# board, aloc, bloc, result = [[1]], [0, 0], [0, 0], 0
# board, aloc, bloc = [[1, 1]], [0, 0], [0, 1]
# board, aloc, bloc = [[1, 1]], [0, 0], [0, 0]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def canmove(board, y, x):
    if 0 <= y < len(board) and 0 <= x < len(board[0]) and board[y][x]:
        return True
    return False


def move(board, y1, x1, y2, x2):
    if not board[y1][x1]:
        return [False, 0]
    cantmove = True
    can_win = False
    max_cnt = 0
    min_cnt = 25
    for i in range(4):
        yy = y1 + dy[i]
        xx = x1 + dx[i]
        
        if not canmove(board, yy, xx): continue
        
        cantmove = False
        board[y1][x1] = 0
        result = move(board, y2, x2, yy, xx)
        board[y1][x1] = 1

        if not result[0]:
            can_win = True
            min_cnt = min(min_cnt, result[1])
        elif not can_win:
            max_cnt = max(max_cnt, result[1])

    if cantmove:
        return [False, 0]
    
    if can_win:
        return [True, min_cnt + 1]
    
    return [False, max_cnt + 1]

    
def solution(board, aloc, bloc):
    
    result = move(board, aloc[0], aloc[1], bloc[0], bloc[1])
    return result[1]


print(solution(board, aloc, bloc))
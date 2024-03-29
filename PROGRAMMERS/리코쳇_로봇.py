'''TC1'''
board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
result = 7
'''TC2'''
board = [".D.R", "....", ".G..", "...D"]
result = -1


TC = 2
board = [["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."], [".D.R", "....", ".G..", "...D"]]
result = [7, -1]


def solution(board):
    N = len(board)
    M = len(board[0])
    check = [[0]*M for _ in range(N)]
    y, x = 0, 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                y, x = i, j

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    check[y][x] = 1
    lst = [[y, x, 0]]
    idx = 0
    while idx < len(lst):
        y, x, n = lst[idx]
        for d in range(4):
            ny = y
            nx = x 
            while 0 <= ny+dy[d] < N and 0 <= nx+dx[d] < M and board[ny+dy[d]][nx+dx[d]] != 'D':
                ny += dy[d]
                nx += dx[d]
            

            if not check[ny][nx]:
                check[ny][nx] = 1
                if board[ny][nx] == 'G':
                    return n+1
                lst.append([ny, nx, n+1])
        
        idx += 1

    return -1


for t in range(TC):
    answer = solution(board[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
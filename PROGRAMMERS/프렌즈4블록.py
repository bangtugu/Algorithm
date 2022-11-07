from collections import deque
from pprint import pprint

answer = 0  # 제거되는 블록 수


def check(m, n, i, j, board):
    Q = deque()
    Q.append((i, j))

    lst = set()

    while Q:
        y, x = Q.popleft()
        y1, x1 = y + 1, x + 1
        if 0 <= y < m and 0 <= y1 < m and 0 <= x < n and 0 <= x1 < n and board[y][x] != 'TARGET' and board[y][x] != 'EMPTY':
            if board[y][x] == board[y][x1] == board[y1][x] == board[y1][x1]:
                Q.append((y, x1))
                Q.append((y1, x))
                Q.append((y1, x1))
                lst.add((i, j))
                lst.add((y, x1))
                lst.add((y1, x))
                lst.add((y1, x1))

    for block in lst:
        board[block[0]][block[1]] = 'TARGET'

    return board


def delete(m, n, board):
    ing = False

    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] != 'TARGET' and board[i][j] != 'EMPTY':
                board = check(m, n, i, j, board)

    block = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'TARGET':
                board[i][j] = 'EMPTY'
                block += 1

    if block:
        global answer
        answer += block
        ing = True

    return board, ing


def down(m, n, board):
    for i in range(m-1):
        for j in range(n):
            if board[i+1][j] == 'EMPTY':
                upstair = board[i][j]
                board[i+1][j] = upstair
                board[i][j] = 'EMPTY'

    return board


def solution(m, n, board):

    for i in range(m):
        board[i] = [board[i][j] for j in range(n)]

    # 높이 m 폭 n
    # 라이언(R) 무지(M) 어피치(A) 프로도(F) 네오(N) 튜브(T) 제이지(J) 콘(C)

    ing = True

    while ing:
        pprint(board)
        board, ing = delete(m, n, board)
        pprint(board)
        if ing:
            board = down(m, n, board)
        pprint(board)

    global answer
    return answer, board


answer, board = solution(6, 6, list(["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(answer)
pprint(board)
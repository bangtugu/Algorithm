board, result = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]], 7


def solution(board):

    N = len(board)    
    M = {
        True : [[N*N] * N for _ in range(N)],
        False : [[N*N] * N for _ in range(N)]
        }
    M[True][0][0] = 0

    from collections import deque
    lst = deque()
    lst.append([0, 0, True])

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    ry = {
        True: [0, 0, -1, -1],
        False: [0, 1, 0, 1]
        }
    rx = {
        True: [0, 1, 0, 1],
        False: [0, 0, -1, -1]
        }
    

    def roll_check(y, x, i, state):
        if i <= 1:
            if y+1 >= N or board[y+1][x] or x+1 >= N or board[y][x+1] or board[y+1][x+1]:
                return False
        elif state:
            if y-1 < 0 or board[y-1][x] or board[y-1][x+1]:
                return False
        else:
            if x-1 < 0 or board[y][x-1] or board[y+1][x-1]:
                return False

        return True


    while lst:
        y, x, state = lst.popleft()
        
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]

            if 0 <= yy < N and 0 <= xx < N and not board[yy][xx] and M[state][yy][xx] > M[state][y][x] + 1:
                if (state and 0 <= xx+1 < N and not board[yy][xx+1]) or (not state and 0 <= yy+1 < N and not board[yy+1][xx]):
                    M[state][yy][xx] = M[state][y][x] + 1
                    lst.append([yy, xx, state])
                
        for i in range(4):
            yy = y + ry[state][i]
            xx = x + rx[state][i]

            if 0 <= yy < N and 0 <= xx < N and not board[yy][xx] and M[not state][yy][xx] > M[state][y][x] + 1:
                if roll_check(y, x, i, state):
                    M[not state][yy][xx] = M[state][y][x] + 1
                    lst.append([yy, xx, not state])

    return min(M[True][N-1][N-2], M[False][N-2][N-1])


print(solution(board))
board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
result = 2


def solution(board):
    N = len(board)
    block_dic = {}
    blocking = {}
    answer = 0

    for i in range(N):
        for j in range(N):
            if not board[i][j]: continue
            if board[i][j] not in block_dic.keys():
                block_dic[board[i][j]] = [True]
                blocking[board[i][j]] = []
            block_dic[board[i][j]].append([i, j])


    def remove_block(n, lst):
    
        miny = 100
        minx = 100
        maxy = 0
        maxx = 0

        for i in range(1, len(lst)):
            y, x = lst[i]
            miny = min(miny, y)
            minx = min(minx, x)
            maxy = max(maxy, y)
            maxx = max(maxx, x)
        
        for i in range(miny, maxy+1):
            for j in range(minx, maxx+1):
                if board[i][j] == 0:
                    for z in range(i, -1, -1):
                        if board[z][j] != 0:
                            blocking[n].append(board[z][j])
                            return False
                elif board[i][j] != key:
                    return False

        block_dic[n][0] = False
        for i in range(1, len(lst)):
            y, x = lst[i]
            board[y][x] = 0

        return True


    solve = True
    while solve:
        solve = False
        for key in block_dic.keys():
            if block_dic[key][0]:
                for block in blocking[key]:
                    if block_dic[block][0]:
                        break
                else:
                    if remove_block(key, block_dic[key]):
                        answer += 1                
                        solve = True

    return answer


print(solution(board))
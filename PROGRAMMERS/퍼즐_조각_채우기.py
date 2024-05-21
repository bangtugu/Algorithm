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


    def get_cntlst(inputlst):
        cnt, lst = 0, []

        for i in range(N):
            for j in range(N):
                if not inputlst[i][j]:
                    cnt += 1
                    inputlst[i][j] = cnt
                    temp = [[i, j]]
                    idx = 0
                    while idx < len(temp):
                        y, x = temp[idx]
                        for d in range(4):
                            ny = y + dy[d]
                            nx = x + dx[d]

                            if nx < 0 or nx >= N or ny < 0 or ny >= N or inputlst[ny][nx]: continue
                            inputlst[ny][nx] = cnt
                            temp.append([ny, nx])

                        idx += 1
                    lst.append(temp)

        return cnt, lst
    

    blank_cnt, blank_lst = get_cntlst(game_board)
    block_cnt, block_lst = get_cntlst(table)


    def rotate(lst):
        cnt = len(lst)
        min_y, min_x = N, N
        max_y, max_x = 0, 0
        for y, x in lst:
            min_y = min(min_y, y)
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

        max_y -= min_y
        max_x -= min_x
        temp = [[0]*(max_x+1) for _ in range(max_y+1)]
        for y, x in lst:
            temp[y-min_y][x-min_x] = 1
        
        rotate_lst = []
        for i in range(4):
            if i%2:
                rotate_lst.append([[0]*(max_y+1) for _ in range(max_x+1)])
            else:
                rotate_lst.append([[0]*(max_x+1) for _ in range(max_y+1)])

        for i in range(max_y+1):
            for j in range(max_x+1):
                rotate_lst[0][i][j] = temp[i][j]
                rotate_lst[1][j][-(i+1)] = temp[i][j]
                rotate_lst[2][-(i+1)][-(j+1)] = temp[i][j]
                rotate_lst[3][-(j+1)][i] = temp[i][j]

        return[cnt, rotate_lst]
    

    for i in range(block_cnt):
        block_lst[i] = rotate(block_lst[i])
    for i in range(blank_cnt):
        blank_lst[i] = rotate(blank_lst[i])
    

    def is_match(lst1, lst2):
        y1 = len(lst1[0])
        x1 = len(lst1[0][0])

        for c in range(len(lst2)):
            y2 = len(lst2[c])
            x2 = len(lst2[c][0])

            if y1 != y2 or x1 != x2: continue

            fail = False
            for i in range(y1):
                if fail: break
                for j in range(x1):
                    if fail: break
                    if lst1[0][i][j] != lst2[c][i][j]:
                        fail = True
            
            if not fail: return True

        return False


    answer = 0
    for i in range(blank_cnt):
        for j in range(block_cnt):
            if not block_lst[j][0]: continue
            if blank_lst[i][0] != block_lst[j][0]: continue
            if is_match(blank_lst[i][1], block_lst[j][1]):
                answer += blank_lst[i][0]
                blank_lst[i][0] = 0
                block_lst[j][0] = 0
                break

    return answer


for t in range(TC):
    answer = solution(game_board[t], table[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
board, r, c, result = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0, 14
# board, r, c, result = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1, 16

def solution(board, r, c):

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    check = {
        0: [False],
        1: [False],
        2: [False],
        3: [False],
        4: [False],
        5: [False],
        6: [False]
    }

    for i in range(4):
        for j in range(4):
            if board[i][j]:
                check[board[i][j]][0] = True
                check[board[i][j]].append([i,j])


    def count(sy, sx, ey, ex):
        if sy == ey and sx == ex:
            return 1

        j = 0
        lst = [[sy, sx, 0]]
        v = [[0]*4 for _ in range(4)]
        v[sy][sx] = 1
        
        while True:
            get_goal = False
            y, x, n = lst[j]
            for z in range(4):
                
                ny = y + dy[z]
                nx = x + dx[z]

                if 0 > ny or ny >= 4 or 0 > nx or nx >= 4: continue
                if not v[ny][nx]:
                    v[ny][nx] = 1
                    lst.append([ny, nx, n+1])

                if ny == ey and nx == ex:
                    get_goal = True
                    break

                while 0 <= ny + dy[z] < 4 and 0 <= nx + dx[z] < 4:
                    if board[ny][nx] and check[board[ny][nx]][0]:
                        break
                    ny += dy[z]
                    nx += dx[z]
                
                if v[ny][nx]: continue
                v[ny][nx] = 1
                lst.append([ny, nx, n+1])

                if ny == ey and nx == ex:
                    get_goal = True
                    break
            
            if get_goal:
                break

            j += 1        

        return lst[-1][2] + 1


    global min_value
    min_value = 999999


    def go(lst, y, x, value):
        global min_value
        if value >= min_value:
            return
        
        if sum(lst) == 0:
            min_value = min(value, min_value)
            return

        for i in range(len(lst)):
            if not lst[i]: continue

            n = lst[i]
            
            y1, x1 = check[n][1]
            y2, x2 = check[n][2]

            s11 = count(y, x, y1, x1)
            s12 = count(y1, x1, y2, x2)
            s21 = count(y, x, y2, x2)
            s22 = count(y2, x2, y1, x1)

            v1 = s11 + s12
            v2 = s21 + s22
            lst[i] = 0
            check[n][0] = False
            go(lst, y2, x2, value+v1)
            go(lst, y1, x1, value+v2)
            check[n][0] = True
            lst[i] = n

        return

    
    lst = []

    for i in check.keys():
        if check[i][0]: lst.append(i)

    go(lst, r, c, 0)

    return min_value


print(solution(board, r, c))
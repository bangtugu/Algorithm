'''TC1'''
board = [[0,0,0],[0,0,0],[0,0,0]]
result = 900
'''TC2'''
board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
result = 3800
'''TC3'''
board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
result = 2100
'''TC4'''
board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
result = 3200


TC = 4
board = [[[0,0,0],[0,0,0],[0,0,0]], [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]], [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]], [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]]
result = [900, 3800, 2100, 3200]


def solution(board):
    
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    dw = [0, 0, 1, 1]
    N = len(board)
    cost = [[[N*N*600, N*N*600]for _ in range(N)]for _ in range(N)]
    
    lst = []
    for j in [0, 2]:
        for i in range(1, N):
            ny = dy[j]*i
            nx = dx[j]*i
            if ny >= N or nx >= N or board[ny][nx] == 1: break
            
            cost[ny][nx][dw[j]] = 100*i
            lst.append([ny, nx])
    
    idx = 0
    while idx < len(lst):
        y, x = lst[idx]
        
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            nw = dw[d]
            if ny < 0 or ny >= N or nx < 0 or nx >= N or board[ny][nx] == 1: continue
            
            newcost = min(cost[y][x][0]+600, cost[y][x][1]+100) if nw else min(cost[y][x][1]+600, cost[y][x][0]+100)
            if cost[ny][nx][nw] > newcost:
                cost[ny][nx][nw] = newcost
                lst.append([ny, nx])
                
        idx += 1

    return min(cost[N-1][N-1])


for t in range(TC):
    answer = solution(board[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
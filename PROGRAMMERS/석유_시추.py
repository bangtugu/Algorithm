'''TC1'''
land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
result = 9
'''TC2'''
land = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
result = 16


TC = 2
land = [[[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]], [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]]
result = [9, 16]


def solution(land):


    from collections import deque

    N = len(land)
    M = len(land[0])
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    def grouping(y, x, g):
        
        Q = deque()
        Q.append([y, x])
        land[y][x] = g
        num = 0

        while Q:
            num += 1    
            ny, nx = Q.popleft()
            
            for i in range(4):
                yy = ny + dy[i]
                xx = nx + dx[i]
                if yy < 0 or yy >= N or xx < 0 or xx >= M or land[yy][xx] == g or land[yy][xx] != 1: continue
                Q.append([yy, xx])
                land[yy][xx] = g
                
        return num
    

    group = [0, 0]
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1:
                group.append(grouping(i, j, len(group)))
    answer = 0

    for j in range(M):
        oilrig = set()
        for i in range(N):
            oilrig.add(land[i][j])
        
        oil = 0
        for g in oilrig:
            oil += group[g]
        
        answer = max(answer, oil)

    return answer


for t in range(TC):
    answer = solution(land[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
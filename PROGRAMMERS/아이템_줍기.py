'''TC1'''
rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX = 1
characterY = 3
itemX = 7
itemY = 8
result = 17
'''TC2'''
rectangle = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]
characterX = 9
characterY = 7
itemX = 6
itemY = 1
result = 11
'''TC3'''
rectangle = [[1,1,5,7]]
characterX = 1
characterY = 1
itemX = 4
itemY = 7
result = 9
'''TC4'''
rectangle = [[2,1,7,5],[6,4,10,10]]
characterX = 3
characterY = 1
itemX = 7
itemY = 10
result = 15
'''TC5'''
rectangle = [[2,2,5,5],[1,3,6,4],[3,1,4,6]]
characterX = 1
characterY = 4
itemX = 6
itemY = 3
result = 10


TC = 5
rectangle = [[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], [[1,1,5,7]], [[2,1,7,5],[6,4,10,10]], [[2,2,5,5],[1,3,6,4],[3,1,4,6]]]
characterX = [1, 9, 1, 3, 1]
characterY = [3, 7, 1, 1, 4]
itemX = [7, 6, 4, 7, 6]
itemY = [8, 1, 7, 10, 3]
result = [17, 11, 9, 15, 10]


def solution(rectangle, characterX, characterY, itemX, itemY):
    
    corner_dic = {}
    lst = [[-1]*51 for _ in range(51)]
    dy = [0, 0, 1, -1, 1, 1, -1, -1]
    dx = [1, -1, 0, 0, 1, -1, 1, -1]

    for i in range(len(rectangle)):
        x1, y1, x2, y2 = rectangle[i]

        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                lst[y][x] = 0


    def outside_check(y, x):
        count = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny >= 51 or ny <= 0 or nx >= 51 or nx <= 0 or lst[ny][nx] == -1: count += 1

        return count
    

    from collections import deque
    Q = deque()
    Q.append([characterY, characterX])
    lst[characterY][characterX] = 1
    while Q:
        print(Q)
        nowy, nowx = Q.popleft()
        if nowy == itemY and nowx == itemX:
            break
        
        way = []
        for d in range(4):
            newy = nowy + dy[d]
            newx = nowx + dx[d]

            if newy >= 51 or newy <= 0 or newx >= 51 or newx <= 0 or lst[newy][newx] == -1: continue
            if not lst[newy][newx] and outside_check(newy, newx): 
                way.append([newy, newx])

        if len(way):        
        lst[newy][newx] = lst[nowy][nowx] + 1
    
    return lst[itemY][itemX]


for t in range(TC):
    answer = solution(rectangle[t], characterX[t], characterY[t], itemX[t], itemY[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
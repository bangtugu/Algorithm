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
    
    lst = [[-1]*51 for _ in range(51)]
    check = [[0]*51 for _ in range(51)]
    dy1 = [0, -1, -1, 0]
    dx1 = [0, 0, -1, -1]
    dy2 = [0, 0, 1, -1]
    dx2 = [1, -1, 0, 0]

    for i in range(len(rectangle)):
        x1, y1, x2, y2 = rectangle[i]
        for y in range(y1, y2):
            for x in range(x1, x2):
                lst[y][x] = 0


    def outside_check(y, x):
        count = [1]*4
        for i in range(4):
            ny = y + dy1[i]
            nx = x + dx1[i]

            if ny >= 51 or ny <= 0 or nx >= 51 or nx <= 0 or lst[ny][nx] == -1: count[i] = 0

        return count
    

    from collections import deque
    Q = deque()
    Q.append([characterY, characterX, outside_check(characterY, characterX)])
    check[characterY][characterX] = 1
    while Q:
        nowy, nowx, nowc = Q.popleft()
        if nowy == itemY and nowx == itemX: break
        
        way = []
        for d in range(4):
            newy = nowy + dy2[d]
            newx = nowx + dx2[d]

            if newy >= 51 or newy <= 0 or newx >= 51 or newx <= 0 or check[newy][newx]: continue
            way.append([newy, newx, outside_check(newy, newx)])

        for newy, newx, newc in way:
            if nowx == newx:
                if nowy < newy:
                    if nowc[0] != nowc[3]:
                        Q.append([newy, newx, newc])
                        check[newy][newx] = check[nowy][nowx] + 1
                else:
                    if nowc[1] != nowc[2]:
                        Q.append([newy, newx, newc])
                        check[newy][newx] = check[nowy][nowx] + 1

            if nowy == newy:
                if nowx < newx:
                    if nowc[0] != nowc[1]:
                        Q.append([newy, newx, newc])
                        check[newy][newx] = check[nowy][nowx] + 1
                else:
                    if nowc[2] != nowc[3]:
                        Q.append([newy, newx, newc])
                        check[newy][newx] = check[nowy][nowx] + 1
    
    return check[itemY][itemX]-1


for t in range(TC):
    answer = solution(rectangle[t], characterX[t], characterY[t], itemX[t], itemY[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
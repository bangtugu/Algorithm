'''TC1'''
m = 10
n = 10
startX = 3
startY = 7
balls = [[7, 7], [2, 7], [7, 3]]
result = [52, 37, 116]


TC = 1
m = [10]
n = [10]
startX = [3]
startY = [7]
balls = [[[7, 7], [2, 7], [7, 3]]]
result = [[52, 37, 116]]


def solution(m, n, startX, startY, balls):
    
    
    def can_corner(n, m, sy, sx, y, x):
        
        dy = sy - y / sx - x
        rev = False
        lst = []
        while 0 < x <= m:
            if rev:
                x -= 1
                y -= dy

            else:
                x += 1
                y += dy
                if x == m:
                    rev = True

            if x == 0 or x == m:
                if y == 0 or y == n:
                    lst.append([y, x])

        return lst
    

    def calc(x1, x2, y):
        return ((x1**2 + (y*x1/(x1+x2))**2)**(1/2) + (x2**2 + (y*x2/(x1+x2))**2)**(1/2))**2
    

    def calc90(num1, num2):
        return (num1+num2)**2


    answer = []    
    for x, y in balls:
        min_v = max(n**3, m**3)
        corner = can_corner(n, m, startY, startX, y, x)
        if corner:
            for yy, xx in corner:
                if yy < y < startY and xx < x < startX:
                    min_v = min(min_v, (((y**2+x**2)**(1/2)+(startY**2+startX**2)**(1/2)))**2)
                if yy > y > startY and xx > x > startX:
                    min_v = min(min_v, (((yy-y)**2+(xx-x)**2)**(1/2)+((yy-startY)**2+(xx-startX)**2)**(1/2))**2)
        
        if not (startX == x and startX < x):
            x1 = m-startX
            x2 = m-x
            y1 = abs(startY-y)
            if startY == y:
                min_v = min(min_v, calc90(x1, x2))
            else:
                min_v = min(min_v, calc(x1, x2, y1))
        
        if not (startX == x and startX > x):
            x1 = startX
            x2 = x
            y1 = abs(startY-y)
            if startY == y:
                min_v = min(min_v, calc90(x1, x2))
            else:
                min_v = min(min_v, calc(x1, x2, y1))

        if not (startY == y and startY < y):
            y1 = n - startY
            y2 = n - y
            x1 = abs(startX-x)
            if x1:
                min_v = min(min_v, calc(y1, y2, x1))
            else:
                min_v = min(min_v, calc90(y1, y2))

        if not (startY == y and startY > y):
            y1 = startY
            y2 = y
            x1 = abs(startX-x)
            if x1:
                min_v = min(min_v, calc(y1, y2, x1))
            else:
                min_v = min(min_v, calc90(y1, y2))

        if min_v > int(min_v):
            answer.append(int(min_v)+1)
        else:
            answer.append(min_v)

    return answer


for t in range(TC):
    answer = solution(m[t], n[t], startX[t], startY[t], balls[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
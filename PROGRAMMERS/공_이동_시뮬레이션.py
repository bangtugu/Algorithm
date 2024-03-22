'''TC1'''
n = 2
m = 2
x = 0
y = 0
queries = [[2,1],[0,1],[1,1],[0,1],[2,1]]
result = 4
'''TC2'''
n = 2
m = 5
x = 0
y = 1
queries = [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]
result = 2


TC = 2
n = [2, 2]
m = [2, 5]
x = [0, 0]
y = [0, 1]
queries = [[[2,1],[0,1],[1,1],[0,1],[2,1]], [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]]
result = [4, 2]


def solution(n, m, y, x, queries):
    
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    lst = [[y, x]]
    for i in range(1, len(queries)+1):
        
        new_lst = []
        d, c = queries[-i]
        
        for j in range(len(lst)):
            nowy, nowx = lst[j]
            
            if nowy + dy[d] < 0 or nowy + dy[d] >= n or nowx + dx[d] < 0 or nowx + dx[d] >= m:
                for z in range(c+1):
                    if 0 <= nowy - dy[d]*z < n and 0 <= nowx - dx[d]*z < m:
                        new_lst.append([nowy - dy[d]*z, nowx - dx[d]*z])
                
            else:
                if 0 <= nowy - dy[d]*c < n and 0 <= nowx - dx[d]*c < m:
                    new_lst.append([nowy-dy[d]*c, nowx-dx[d]*c])
        
        lst = new_lst
        
    return len(lst)


def solution(n, m, y, x, queries):
    
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    y1 = x1 = 0
    y2, x2 = n-1, m-1

    lt, mt, rt = 1, 1, 1
    lm, mm, rm = 1, 1, 1
    lb, mb, rb = 1, 1, 1

    for d, c in queries:
        
        for _ in range(c):
            if d == 0:
                if x1 == 0:
                    if x1 == x2: continue
                    elif x1+1 == x2:
                        lt += mt
                        lm += mm
                        lb += mb
                    else:
                        lt += rt
                        rt = mt = lt
                        lm += rm
                        rm = mm = lm
                        lb += rb
                        rb = mb = lb
                    x2 -= 1
                else:
                    x1 -= 1
                    x2 -= 1

            elif d == 1:
                if x2 == m-1:
                    if x2 == x1: continue
                    elif x1+1 == x2:
                        rt += mt
                        rm += mm
                        rb += mb
                    else:
                        rt += lt
                        lt = mt = rt
                        rm += lm
                        lm = mm = rm
                        rb += lb
                        lb = mb = rb
                    x1 += 1
                else:
                    x1 += 1
                    x2 += 1

            elif d == 2:
                if y1 == 0:
                    if y1 == y2: continue
                    elif y1+1 == y2:
                        lt += lm
                        mt += mm
                        rt += rm
                    else:
                        lt += lb
                        lb = lm = lt
                        mt += mb
                        mb = mm = mt
                        rt += rb
                        rb = rm = rt
                    y2 -= 1
                else:
                    y1 -= 1
                    y2 -= 1

            else:
                if y2 == n-1:
                    if y2 == y1: continue
                    elif y1+1 == y2:
                        lb += lm
                        mb += mm
                        rb += rm
                    else:
                        lb += lt
                        lt = lm = lb
                        mb += mt
                        mt = mm = mb
                        rb += rt
                        rt = rm = rb
                    y1 += 1
                else:
                    y1 += 1
                    y2 += 1
        
    lst = [
        [lt, mt, rt],
        [lm, mm, rm],
        [lb, mb, rb]
        ]
    
    print(y, x)
    print(y1, y2, x1, x2)
    print(lst)

    if y < y1 or x < x1 or y > y2 or x > x2: return 0
    

    yy = xx = 0
    if y == y1:
        yy = 0
    elif y == y2:
        yy = 2
    else:
        yy = 1
    
    if x == x1:
        xx = 0
    elif x == x2:
        xx = 2
    else:
        xx = 1
    print(yy, xx)
    return lst[yy][xx]


for t in range(TC):
    answer = solution(n[t], m[t], x[t], y[t], queries[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
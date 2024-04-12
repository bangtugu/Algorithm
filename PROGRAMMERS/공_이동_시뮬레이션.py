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


def solution(n, m, y, x, queries):
    
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    ymin = [0, 1]
    ymax = [n-1, 1]
    xmin = [0, 1]
    xmax = [m-1, 1]
    ysame = [False, 0, n]
    xsame = [False, 0, m]

    for d, c in queries:
        
        if d > 1:
            if ysame[0]:
                ysame[1] += dy[d]*c
                ysame[1] = max(ysame[1], 0)
                ysame[1] = min(ysame[1], n-1)

            else:
                ymin[0] += dy[d]*c
                ymax[0] += dy[d]*c
                
                if ymin[0] < 0:
                    ymin[1] -= ymin[0]
                    ymin[0] = 0
                if ymax[0] >= n:
                    ymax[1] += ymax[0]-n+1
                    ymax[0] = n-1

                if ymin[0] >= ymax[0]:
                    ysame[0] = True
                    ysame[1] = n-1 if xmin[0] else 0

        else:
            if xsame[0]:
                xsame[1] += dx[d]*c
                xsame[1] = max(xsame[1], 0)
                xsame[1] = min(xsame[1], m-1)

            else:
                xmin[0] += dx[d]*c
                xmax[0] += dx[d]*c
                
                if xmin[0] < 0:
                    xmin[1] -= xmin[0]
                    xmin[0] = 0
                if xmax[0] >= n:
                    xmax[1] += xmax[0]-m+1
                    xmax[0] = m-1

                if xmin[0] >= xmax[0]:
                    xsame[0] = True
                    xsame[1] = m-1 if xmin[0] else 0

    if ysame[0]:
        if y == ysame[1]:
            yv = ysame[2]
        else:
            return 0
    else:
        if y == ymin[0]:
            yv = ymin[1]
        elif y == ymax[0]:
            yv = ymax[1]
        elif ymin[0] < y < ymax[0]:
            yv = 1
        else:
            return 0

    if xsame[0]:
        if x == xsame[1]:
            xv = xsame[2]
        else:
            return 0
    else:
        if x == xmin[0]:
            xv = xmin[1]
        elif x == xmax[0]:
            xv = xmax[1]
        elif xmin[0] < x < xmax[0]:
            xv = 1
        else:
            return 0

    answer = yv * xv
    return answer


def solution(n, m, y, x, queries):
    
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    ymin = [0, 1]
    ymax = [n-1, 1]
    xmin = [0, 1]
    xmax = [m-1, 1]
    ysame = [False, 0]
    xsame = [False, 0]

    for d, c in queries:
        
        if d > 1:
            tmin, tmax, tvmax, tsame, dt = ymin, ymax, n, ysame, dy
        else:
            tmin, tmax, tvmax, tsame, dt = xmin, xmax, m, xsame, dx

        if tsame[0]:
            tsame[1] += dt[d]*c
            tsame[1] = max(tsame[1], 0)
            tsame[1] = min(tsame[1], tvmax-1)

        else:
            for t in [tmin, tmax]:
                t[0] += dt[d]*c

                if t[0] < 0:
                    t[1] -= t[0]
                    t[0] = 0
                if t[0] >= tvmax:
                    t[1] += t[0]-tvmax+1
                    t[0] = tvmax-1

            if tmin[0] >= tmax[0]:
                tsame[0] = True
                tsame[1] = tvmax-1 if tmin[0] else 0

    yv = [0]
    xv = [0]
    for tmin, tmax, tsame, tv, t, tvmax in [[ymin, ymax, ysame, yv, y, n], [xmin, xmax, xsame, xv, x, m]]:
        if tsame[0]:
            if t == tsame[1]:
                tv[0] = tvmax
            else:
                return 0
        else:
            if t == tmin[0]:
                tv[0] = tmin[1]
            elif t == tmax[0]:
                tv[0] = tmax[1]
            elif tmin[0] < t < tmax[0]:
                tv[0] = 1
            else:
                return 0

    answer = yv[0] * xv[0]
    return answer


for t in range(TC):
    answer = solution(n[t], m[t], x[t], y[t], queries[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
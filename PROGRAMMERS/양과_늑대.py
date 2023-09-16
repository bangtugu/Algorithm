# info, edges, result = [0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]], 5
# info, edges, result = [0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]], 5
info = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16]]
Return = 17
'''
2 ≤ info의 길이 ≤ 17
edges의 세로(행) 길이 = info의 길이 - 1
'''

def solution1(info, edges):
    
    for i in range(len(info)):
        if info[i]:
            info[i] = [1, 0, 1]
        else:
            info[i] = [0, 1, 0]

    ptc = [[] for _ in range(len(info))]
    ctp = [[] for _ in range(len(info))]
    
    for edge in edges:
        p, c = edge
        ptc[p].append(c)
        ctp[c].append(p)
    
    depth = [[]]
    temp = [0,'d']
    i = 0
    while i < len(temp)-1:
        if temp[i] == 'd':
            temp.append('d')
            depth.append([])
        
        else:
            now = temp[i]
            depth[-1].append(now)
            temp.extend(ptc[now])

        i += 1

    # for i in range(len(depth)-1, -1, -1):
    #     for c in depth[i]:
    #         if info[c][0]:
    #             for p in ctp[c]:
    #                 if info[p][1] == 0: continue
    #                 info[p][0] += info[c][0]
    #                 info[p][1] += info[c][1]

    for i in range(len(depth)-1, -1, -1):
        for c in depth[i]:
            if not info[c][1]: continue
            p = ctp[c]
            info[p][1] 

    print(info)

    s = 0
    temp = [0]
    i = 0
    while i < len(temp):
        if not info[temp[i]]:
            s += 1
            temp.extend(ptc[temp[i]])

        i += 1

    return s




max_s = 1
v_set = set()
v = [1] + [0]*16


def solution2(info, edges):
    
    ptc = [[] for _ in range(len(info))]

    for edge in edges:
        p, c = edge
        ptc[p].append(c)
    
    
    def check(s, w):
        
        if w == s:
            return
        
        global max_s, v, v_set
        max_s = max(s, max_s)
        
        lst = []
        for i in range(len(info)):
            if not v[i]: continue
            for c in ptc[i]:
                if v[c]: continue
                lst.append(c)

        for i in lst:
            if v[i]: continue
            v[i] = 1
            v_str = ''
            for alp in map(str, v):
                v_str = v_str + alp
            if v_str not in v_set:
                v_set.add(v_str)
                if info[i]:
                    check(s, w+1)
                else:
                    check(s+1, w)
            v[i] = 0

                
    check(1, 0)
    
    global max_s
    return max_s


print(solution2(info, edges))
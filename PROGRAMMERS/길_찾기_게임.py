nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
result = [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]


def solution(nodeinfo):
    level = {}
    max_value = 0
    node_num = {}

    for i in range(len(nodeinfo)):
        x, y = nodeinfo[i]
        if y not in level.keys():
            level[y] = []
        level[y].append(x)
        max_value = max(max_value, x)
        node_num[x] = i+1

    level_key = sorted(level.keys(), reverse=True)
    for key in level_key:
        level[key].sort()

    p = [-1] * (max_value + 1)
    c = [[-1, -1] for _ in range(max_value + 1)]
    

    def can_child(P, C):
        ps = [P, C]
        while p[P] != -1:
            ps.append(p[P])
            P = p[P]

        P = ps[0]
        ps.sort()
        idx = ps.index(C) if C < P else ps.index(P)

        if ps[idx+1] == C or ps[idx+1] == P:
            return True
        return False
        

    for i in range(1, len(level_key)):
        plst = level[level_key[i-1]]
        clst = level[level_key[i]]
        pidx = 0
        cidx = 0
        while cidx < len(clst):
            P, C = plst[pidx], clst[cidx]
            if can_child(P, C):
                p[C] = P
                if P > C:
                    c[P][0] = C
                else:
                    c[P][1] = C
                cidx += 1
            else:
                pidx += 1
        
    from sys import setrecursionlimit
    setrecursionlimit(10001)


    def preorder(node, lst):
        lst.append(node_num[node])
        for C in c[node]:
            if C != -1:
                lst = preorder(C, lst)
        return lst


    def postorder(node, lst):
        for C in c[node]:
            if C != -1:
                lst = postorder(C, lst)
        lst.append(node_num[node])
        return lst


    leaf = level[level_key[0]][0]
    return [preorder(leaf, []), postorder(leaf, [])]


print(solution(nodeinfo))
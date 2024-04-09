'''TC1'''
a = [-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]
result = 9
'''TC2'''
a = [0,1,0]
edges = [[0,1],[1,2]]
result = -1


TC = 2
a = [[-5,0,2,1,2], [0,1,0]]
edges = [[[0,1],[3,4],[2,3],[0,3]], [[0,1],[1,2]]]
result = [9, -1]


def solution(a, edges):
    
    if sum(a): return -1
    N = len(a)
    node_graph = [[0]*N for _ in range(N)]
    node_cnt = [0]*N
    node_lst = [[] for _ in range(N)]

    for i, j in edges:
        node_graph[i][j] = 1
        node_graph[j][i] = 1
        node_lst[i].append(j)
        node_lst[j].append(i)
        node_cnt[i] += 1
        node_cnt[j] += 1
    

    def check_min(N, l):
        cnt = N
        lst = []

        for i in range(N):
            if l[i] == 0: continue
            if l[i] < cnt:
                cnt = l[i]
                lst = [i]
            elif l[i] == cnt:
                lst.append(i)
        
        if cnt > 1: return False, []
        return cnt, lst


    answer = 0
    min_cnt, min_lst = check_min(N, node_cnt)
    while min_cnt == 1:
        
        for i in min_lst:
            if not node_cnt[i]: continue
            answer += abs(a[i])
            node_cnt[i] -= 1
            for j in node_lst[i]:
                if not node_cnt[j]: continue
                node_cnt[j] -= 1
                node_graph[i][j] = node_graph[j][i] = 0
                a[j] += a[i]
                a[i] = 0
                break
        
        min_cnt, min_lst = check_min(N, node_cnt)
    
    return answer


def solution(a, edges):

    if sum(a): return -1

    N = len(a)
    check_lst = [0] * N
    node_lst = [[] for _ in range(N)]

    for i, j in edges:
        node_lst[i].append(j)
        node_lst[j].append(i)
    
    depth = 0
    check_lst[0] = 1
    depth_lst = [[0]]

    while depth_lst[depth]:
        new_lst = []

        for i in depth_lst[depth]:
            for j in node_lst[i]:
                if check_lst[j]: continue
                check_lst[j] = 1
                new_lst.append(j)
        
        depth_lst.append(new_lst)
        depth += 1
    
    answer = 0
    for d in range(depth, 0, -1):
        for i in depth_lst[d]:
            for j in node_lst[i]:
                if not check_lst[j]: continue
                answer += abs(a[i])
                a[j] += a[i]
                a[i] = 0
                break
            check_lst[i] = 0

    return answer


for t in range(TC):
    answer = solution(a[t], edges[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
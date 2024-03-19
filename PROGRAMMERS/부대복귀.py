'''TC1'''
n = 3
roads = [[1, 2], [2, 3]]
sources = [2, 3]
destination = 1
result = [1, 2]
'''TC2'''
n = 5
roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
sources = [1, 3, 5]
destination = 5
result = [2, -1, 0]


TC = 2
n = [3, 5]
roads = [[[1, 2], [2, 3]], [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]]
sources = [[2, 3], [1, 3, 5]]
destination = [1, 5]
result = [[1, 2], [2, -1, 0]]


def solution(n, roads, sources, destination):

    network = [set() for _ in range(n+1)]
    for a, b in roads:
        network[a].add(b)
        network[b].add(a)
    
    reach = [-1]*(n+1)
    from collections import deque
    check = set()
    Q = deque()
    Q.append(destination)
    check.add(destination)
    reach[destination] = 0
    while Q:
        now = Q.popleft()
        for way in network[now]:
            if way in check: continue
            check.add(way)
            reach[way] = reach[now] + 1
            Q.append(way)
    
    answer = []
    for source in sources:
        answer.append(reach[source])
    
    return answer


for t in range(TC):
    answer = solution(n[t], roads[t], sources[t], destination[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
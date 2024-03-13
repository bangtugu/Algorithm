'''TC1'''
edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
result = [2, 1, 1, 0]
'''TC2'''
edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
result = [4, 0, 1, 2]


TC = 2
edges = [[[2, 3], [4, 3], [1, 1], [2, 1]], [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]]
result = [[2, 1, 1, 0], [4, 0, 1, 2]]


def solution(edges):
    
    connected = [[0, 0]]

    for a, b in edges:
        if max(a, b) > len(connected)-1:
            for _ in range(max(a, b)-len(connected)+1):
                connected.append([0, 0])
        connected[a][0] += 1
        connected[b][1] += 1
    
    #[생성정점, 도넛, 막대, 8자]
    answer = [0, 0, 0, 0]

    for i in range(1, len(connected)):
        if connected[i][0] == 0:
            answer[2] += 1
        elif connected[i][1] == 0 and connected[i][0] > 1:
            answer[0] = i
        elif connected[i][0] == 2:
            answer[3] += 1

    answer[1] = connected[answer[0]][0] - answer[3] - answer[2]

    return answer


for t in range(TC):
    answer = solution(edges[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, correct, comment))
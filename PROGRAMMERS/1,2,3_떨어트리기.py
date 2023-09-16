# edges = [[2, 4], [1, 2], [6, 8], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9]]
# target = [0, 0, 0, 3, 0, 0, 5, 1, 2, 3]
# result = [1, 1, 2, 2, 2, 3, 3]

# edges = [[1, 2], [1, 3]]
# target = [0, 7, 3]
# result = [1, 1, 3, 2, 3]

edges = [[1, 3], [1, 2]]
target = [0, 7, 1]
result = [-1]


def solution(edges, target):
    
    target = [0] + target
    
    min_cnt = []
    for num in target:
        if num%3:
            min_cnt.append(num//3 + 1)
        else:
            min_cnt.append(num//3)
    
    graph = [[] for _ in range(len(target))]
    for p, c in edges:
        graph[p].append(c)
    
    for i in range(len(graph)):
        if graph[i]:
            graph[i].sort()

    road_num = [0] * len(target)
    cnt = [0] * len(target)
    turn = []


    def check():
        for i in range(len(cnt)):
            if cnt[i] < min_cnt[i]:
                return True
        
        return False


    def next_road(n):
        if graph[n]:
            now = graph[n][road_num[n]]
            road_num[n] += 1
            road_num[n] = road_num[n]%len(graph[n])
            return next_road(now)
        else:
            return n


    while True:
        now = next_road(1)

        turn.append(now)
        cnt[now] += 1

        if cnt[now] > target[now]:
            return [-1]
        
        if check(): continue

        break
    
    answer = [0] * len(turn)
    for i in range(len(cnt)):

        if cnt[i]:
            temp = [1] * cnt[i]

            idx = -1
            while sum(temp) < target[i]:
                if temp[idx] >= 3:
                    idx -= 1
                temp[idx] += 1

            idx = 0
            for j in range(len(turn)):
                
                if turn[j] == i:
                    answer[j] = temp[idx]
                    idx += 1

    return answer


print(solution(edges, target))
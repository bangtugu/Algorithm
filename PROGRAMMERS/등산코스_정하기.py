# n = 6
# paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
# gates = [1, 3]
# summits = [5]

n = 7
paths = [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]
gates = [1]
summits = [2, 3, 4]

# n = 7
# paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
# gates = [3, 7]
# summits = [1, 5]

# n = 5
# paths = [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]]
# gates = [1, 2]
# summits = [5]

'''
각 gate -> summit -> 출발한 gate로 돌아오는거 구하기 = summit -> 각 gate로 내려가는거만 구하기 or gate -> 각 summit으로 올라가는거만 구하기
단순하게 재귀로 각 summit에서 gate 가는 intensity 구하기
맞는 코드여도 시간초과 걸릴 예정
'''

'''
1
'''

def solution1(n, paths, gates, summits):

    answer_summit = n + 1
    answer_intensity = 10000001

    import sys
    sys.setrecursionlimit(10000)

    table = [[0] * (n + 1) for _ in range(n + 1)]

    for s, e, l in paths:
        table[s][e] = table[e][s] = l


    def pathfinding(path_lst, now):

        # print(path_lst, now)

        if now in gates:
            now_intensity = 0
            for i in range(len(path_lst)-1):
                now_intensity = max(now_intensity, table[path_lst[i]][path_lst[i+1]])

            
            if answer_intensity > now_intensity:
                # print(path_lst)
                answer_intensity = now_intensity
                answer_summit = path_lst[0]
            
            return
        
        if now != path_lst[0] and now in summits:
            return
        
        for i in range(n+1):
            if 0 < table[now][i] < answer_intensity and i not in path_lst:
                pathfinding(path_lst+[i], i)

    for summit in summits:
        pathfinding([summit], summit)

    return [answer_summit, answer_intensity]



'''
다익스트라 응용해서
리스트 s_intensity에 출발 summit으로부터의 최소 intensity를 저장해나가는 방식으로
'''

'''
2
'''
def solution2(n, paths, gates, summits):

    gates = set(gates)
    summits.sort()
    summits = set(summits)

    answer_summit = 0
    answer_intensity = 10000001

    path_lst = [[] for _ in range(n + 1)]

    for path in paths:
        path_lst[path[0]].append([path[1], path[2]])
        path_lst[path[1]].append([path[0], path[2]])

    def stg(s):
        s_intensity = [0] * (n + 1)
        lst = [s]
        i = 0

        while i < len(lst):

            now = lst[i]
            if s_intensity[now] >= answer_intensity: i += 1; continue
            for path, inten in path_lst[now]:
                if path not in summits and inten < answer_intensity:
                    if not s_intensity[path] or s_intensity[path] > max(s_intensity[now], inten):
                        s_intensity[path] = max(s_intensity[now], inten)
                        # if path[0] not in gates:
                        if path not in gates and s_intensity[path] < answer_intensity:
                            lst.append(path)

            i += 1

        min_i = 10000001

        for gate in gates:
            # min_i = min(min_i, s_intensity[gate])
            min_i = min(min_i, s_intensity[gate]) if s_intensity[gate] != 0 else min_i

        return min_i

    for summit in summits:
        temp_i = stg(summit)
        if temp_i < answer_intensity:
            answer_summit = summit
            answer_intensity = temp_i
        elif temp_i == answer_intensity:
            answer_summit = min(summit, answer_summit)

    return [answer_summit, answer_intensity]


'''
tc 25개중
10개 통과
8개 실패
7개 시간초과

시간초과는 그렇다치고 실패는 어떤부분에서 나오는거지...
118번째 줄 for문에서 해당 summit에서 gate까지 도달하지 못해 s_intensity[gate]가 0인 경우를 예외처리하니 7개가 통과되었다.

17개 통과
1개 실패
7개 시간초과

1개는 왜틀린거지...
같은 intensity를 가질 경우 낮은 번호의 summit을 반환해야되는데, summits가 오름차순으로 정렬되지 않았을경우 높은 번호의 summit이 반환될 수 있었다.
당연하게 summits가 정렬돼있을거라고 생각한 실수..
summits을 정렬해주니 나머지 1개도 통과됐다.

18개 통과
7개 시간초과

아악 시간초과!

answer_intensity의 값을 참고하면서 가지를 치면 유의미하게 빨라질 수 있을까?

stg 함수의 탐색 리스트에 갱신된 path를 append하는 코드에 해당 path까지의 최소 intensity가 이미 answer_intensity를 넘은 경우를 가지치기 하자 3개의 tc가 통과되었다. (111)

21개 통과
4개 시간초과

105번째 줄에 answer_intensity를 이용해서 한번 더 가지치기를 했더니 2개의 tc가 통과됐다.

23개 통과
2개 시간초과

'''


'''
3
'''
def solution3(n, paths, gates, summits):    
    
    gates = set(gates)
    summits = set(summits)

    answer_summit = 0
    answer_intensity = 10000001

    path_lst = [[] for _ in range(n + 1)]

    for path in paths:
        path_lst[path[0]].append([path[1], path[2]])
        path_lst[path[1]].append([path[0], path[2]])

    intensity = [10000001] * (n + 1)

    lst = list(gates)
        
    for gate in gates:
        intensity[gate] = 0
    
    i = 0
    
    while i < len(lst):

        temp = set()
        
        while i < len(lst):
        
            now = lst[i]
        
            for path, inten in path_lst[now]:
                if path in gates:
                    continue
                
                if intensity[path] > max(intensity[now], inten):
                    intensity[path] = max(intensity[now], inten)
                    
                    if path not in summits:
                        temp.add(path)
            
            i += 1
        
        lst = list(temp)
        i = 0
        
    for summit in summits:
        if intensity[summit] > answer_intensity:
            continue
        elif intensity[summit] == answer_intensity:
            answer_summit = min(answer_summit, summit)
        else:
            answer_summit = summit
            answer_intensity = min(answer_intensity, intensity[summit])
            
    return answer_summit, answer_intensity


print(solution3(n, paths, gates, summits))

'''
맨 처음 출발지를 summit으로 정한 이유 : 가장 작은 summit 번호를 찾기 쉬울거라 생각해서. 
(summits을 오름차순으로 탐색하면서 최소 intensity가 같을 땐 다음 summit을 무시하고 작을때만 갱신하면 되니까)

그런데 개별 summit에서 모든 gate까지의 intensity를 탐색하고 최소 intensity를 반환하는 과정을 summit 갯수만큼 반복하는것보다
모든 gate에서 동시에 출발해서 모든 summit까지의 intensity를 한 번에 구하고 최소intensity summit을 구하는 게 빨랐다.

그리고 25번 tc 진짜 계속 시간초과 났는데 gates랑 summits 둘 다 set 해주니까 전체적으로 엄청 빨라지고 바로 통과됐다.
set으로 걸러주지 않으면 안될 만큼 gate, summit 번호가 엄청 중복된건가? 만약 그렇다면 2번 코드에서 summits 정렬하는데도 엄청 오래 걸렸겠다.
'''
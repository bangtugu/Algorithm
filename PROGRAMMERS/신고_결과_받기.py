id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
result = [2,1,1,0]

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3
# result = [0,0]


def solution(id_list, report, k):

    n = len(id_list)
    id_idx = {}

    for i in range(n):
        id_idx[id_list[i]] = i

    lst = [[0 for _ in range(n)] for _ in range(n)]
    
    for string in report:
        id1, id2 = string.split()
        idx1, idx2 = id_idx[id1], id_idx[id2]
        lst[idx2][idx1] = 1
    
    answer = [0] * n
    for i in range(n):
        if sum(lst[i]) >= k:
            for j in range(n):
                if lst[i][j]:
                    answer[j] += 1    

    return answer


print(solution(id_list, report, k))
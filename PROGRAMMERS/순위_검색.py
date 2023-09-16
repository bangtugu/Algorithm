info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
result = [1,1,1,1,2,4]


def solution(info, query):

    entity = {
        "-" : 0,
        "java" : 1,
        "python" : 2,
        "cpp" : 3,
        "backend" : 1,
        "frontend" : 2,
        "junior" : 1,
        "senior" : 2,
        "pizza" : 1,
        "chicken" : 2
    }

    info_lst = [[[[[] for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(4)]
    
    for i in range(len(info)):
        a, b, c, d, e = list(info[i].split())
        a, b, c, d, e = entity[a], entity[b], entity[c], entity[d], int(e)
        
        for a in [0, a]:
            for b in [0, b]:
                for c in [0, c]:
                    for d in [0, d]:
                        info_lst[a][b][c][d].append(e)
    
    for a in range(4):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    info_lst[a][b][c][d].sort(reverse=True)
    
    answer = []
    for i in range(len(query)):
        q = list(query[i].split())
        a, b, c, d, e = entity[q[0]], entity[q[2]], entity[q[4]], entity[q[6]], int(q[7])
        
        l = 0
        num = len(info_lst[a][b][c][d])
        r = num - 1

        while l <= r:
            m = (l + r) // 2
            if info_lst[a][b][c][d][m] >= e:
                l = m + 1
            
            else:
                num = m
                r = m - 1
        
        answer.append(num)

    return answer



print(solution(info, query))
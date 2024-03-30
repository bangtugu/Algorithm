'''TC1'''
n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
result = 3


TC = 1
n = [6]
vertex = [[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]]
result = [3]


def solution(n, edge):
    
    cnt = [n*10]*(n+1)
    road = [[] for _ in range(n+1)]

    for s, e in edge:
        road[s].append(e)
        road[e].append(s)
    
    cnt[1] = 0
    idx = 0
    check = [1]
    while idx < n+1 and idx < len(check):
        now = check[idx]

        for num in road[now]:
            if cnt[now]+1 < cnt[num]:
                check.append(num)
                cnt[num] = cnt[now]+1

        idx += 1

    max_cnt = 0
    answer = 0
    for num in cnt:
        if num == n*10: continue
        if num > max_cnt:
            max_cnt = num
            answer = 1
        elif num == max_cnt:
            answer += 1
    
    return answer


for t in range(TC):
    answer = solution(n[t], vertex[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
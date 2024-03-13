scores = [[2,2],[1,4],[3,2],[3,2],[2,1]]
result = 4


def solution(scores):
    
    A, B = scores[0]
    
    score_dic = {}

    for a, b in scores:
        if a > A and b > B: return -1
        
        if a+b <= A+B: continue

        if a-b not in score_dic.keys():
            score_dic[a-b] = [a+b, 1]
            continue
        
        if a+b > score_dic[a-b][0]:
            score_dic[a-b] = [a+b, 1]
        elif a+b == score_dic[a-b][0]:
            score_dic[a-b][1] += 1
    
    fail = set()
    key_lst = list(score_dic.keys())
    K = len(key_lst)

    for i in range(K):
        
        k1 = key_lst[i]
        a1 = (score_dic[k1][0] + k1) // 2
        b1 = score_dic[k1][0] - a1

        for j in range(i+1, K):

            k2 = key_lst[j]
            a2 = (score_dic[k2][0] + k2) // 2
            b2 = score_dic[k2][0] - a2

            if a1 < a2 and b1 < b2:
                fail.add(k1)
                continue
            if a2 < a1 and b2 < a2:
                fail.add(k2)

    answer = 1
    for key in key_lst:
        if key in fail: continue
        answer += score_dic[key][1]
        
    return answer



def solution(scores):
    
    A, B = scores[0]
    answer = 1
    temp = 0
    scores.sort(key=lambda s: (-s[0], s[1]))
    for a, b in scores:
        if a > A and b > B: return -1
        if temp <= b:
            if A+B < a+b:
                answer += 1
            temp = b

    return answer


print(solution(scores))

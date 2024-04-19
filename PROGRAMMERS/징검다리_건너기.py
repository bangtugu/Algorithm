'''TC1'''
stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
result = 3


TC = 1
stones = [[2, 4, 5, 3, 2, 1, 4, 2, 5, 1]]
k = [3]
result = [3]


def cross(lst, k):

    cases = len(lst)-k+1
    
    if cases <= 0:
        return max(lst)
    
    value = max(lst[0:k])
    cnt = 0
    for i in range(k):
        lst[0:k].count(value)
    
    for i in range(k, len(lst)):

        if lst[i-k] >= value:
            cnt -= 1
        if lst[k] >= value:
            cnt += 1
        
        if cnt <= 0:
            value = max(lst[i-k+1:i+1])
            cnt = lst[i-k+1:i+1].count(value)
    
    return value


def cross(lst, k):

    cases = len(lst)-k+1
    
    if cases <= 0:
        return max(lst)
    
    max_v = max(lst[0:k])
    now = max_v
    for i in range(1, cases):
        if lst[i+k-1] > now:
            now = lst[i+k-1]
            continue
        if lst[i-1] == now:
            now = max(lst[i:i+k])
            if now < max_v:
                max_v = now
    
    return max_v


def cross(lst, k):

    from collections import deque
    answer = max(lst)
    Q = deque()

    for i in range(len(lst)):
        
        while Q:
            if lst[i] > lst[Q[-1]]:
                Q.pop()
            else:
                break
        
        Q.append(i)

        while Q:
            if Q[0] <= i-k:
                Q.popleft()
            else:
                break
        
        if i >= k-1:
            answer = min(answer, lst[Q[0]])
    
    return answer


def solution(stones, k):
    answer = cross(stones, k)
    return answer


for t in range(TC):
    answer = solution(stones[t], k[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
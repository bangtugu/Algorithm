'''TC1'''
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
result = 4
'''TC2'''
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
result = 0


TC = 2
begin = ["hit", "hit"]
target = ["cog", "cog"]
words = [["hot", "dot", "dog", "lot", "log", "cog"], ["hot", "dot", "dog", "lot", "log"]]
result = [4, 0]


def solution(begin, target, words):
    sett = set(words)
    if target not in sett: return 0
    
    N = len(words)
    M = len(begin)
    
    for i in range(N):
        if words[i] == target:
            words.pop(i)
            break
    words = [begin] + words + [target]
    N = len(words)
    table = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            if i == j: continue
            cnt = 0
            str1 = words[i]
            str2 = words[j]

            for z in range(M):
                if str1[z] == str2[z]: cnt += 1

            if cnt != M-1: continue
            
            table[i].append(j)
            table[j].append(i)

    check = [0]*N
    check[0] = 1
    idx = 0
    lst = [[0, 0]]
    while idx < len(lst):
        now, cnt = lst[idx]
        if now == N-1: return cnt
        for S in table[now]:
            if check[S]: continue
            check[S] = 1
            lst.append([S, cnt+1])
        idx += 1

    return 0


for t in range(TC):
    answer = solution(begin[t], target[t], words[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
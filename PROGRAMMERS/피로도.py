'''TC1'''
k = 80
dungeons = [[80,20],[50,40],[30,10]]
result = 3


TC = 1
k = [80]
dungeons = [[[80,20],[50,40],[30,10]]]
result = [3]


def solution(k, dungeons):
    
    N = len(dungeons)

    def check(k, n, lst):
        answer = 0
        
        for i in range(N):
            if lst[i]: continue
            if k < dungeons[i][0]: continue
            lst[i] = 1
            answer = max(answer, check(k - dungeons[i][1], n+1, lst))
            lst[i] = 0

        return max(answer, sum(lst))

    return check(k, 0, [0]*N)


for t in range(TC):
    answer = solution(k[t], dungeons[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
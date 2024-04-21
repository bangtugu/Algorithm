'''TC1'''
n = 6
times = [7, 10]
result = 28


TC = 1
n = [6]
times = [[7, 10]]
result = [28]


def solution(n, times):
    
    
    def check(num):
        cnt = 0
        for t in times:
            cnt += num//t

        if cnt >= n: return True
        return False


    s = 0
    e = n*max(times)
    now = (s+e)//2
    while s < e:
        now = (s+e)//2
        if check(now):
            e = now
        else:
            s = now+1
    
    return e


for t in range(TC):
    answer = solution(n[t], times[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
'''TC1'''
jobs = [[0, 3], [1, 9], [2, 6]]
result = 9


TC = 1
jobs = [[[0, 3], [1, 9], [2, 6]]]
result = [9]


def solution(jobs):
    
    jobs.sort(key = lambda x : [x[0], x[1]])
    now = 0
    elst = [0]*len(jobs)
    lst = []
    i = 0
    while i < len(jobs):
        if not lst and now <= jobs[i][0]:
            now = sum(jobs[i])
            elst[i] = now
            i += 1
        else:
            if jobs[i][0] <= now:
                lst.append([i, jobs[i][1]])
                i += 1
            else:
                lst.sort(key = lambda x: x[1])
                idx, cost = lst.pop(0)
                now += cost
                elst[idx] = now

    lst.sort(key = lambda x: x[1])
    while lst:
        idx, cost = lst.pop(0)
        now += cost
        elst[idx] = now
    
    return (sum(elst)-sum(jobs[i][0] for i in range(len(jobs))))//len(jobs)


for t in range(TC):
    answer = solution(jobs[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
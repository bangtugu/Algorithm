'''TC1'''
target = 21
result = [1,0]
'''TC2'''
target = 58
result = [2,2]


TC = 2
target = [21, 58]
result = [[1,0], [2,2]]


def solution(target):
    dp = [[-1, -1] for i in range(target+1)]
    single = list(range(1, 21))
    double = set()
    for s in single:
        if s*2 > 20:
            double.add(s*2)
        if s*3 > 20:
            double.add(s*3)
    single.append(50)
    double = sorted(list(double))

    for i in range(1, target+1):
        if i in single:
            dp[i] = [1, 1]
            continue
        elif i in double:
            dp[i] = [1, 0]
            continue

        count = target
        single_count= 0
        for j in range(max(1, i-60), i):
            if j <= 0: continue
            
            if j in single:
                nowc = dp[i-j][0]+1
                nowsc = dp[i-j][1]+1
            elif j in double:
                nowc = dp[i-j][0]+1
                nowsc = dp[i-j][1]
            else:
                nowc = dp[i-j][0]+dp[j][0]
                nowsc = dp[i-j][1]+dp[j][1]

            if nowc < count:
                count, single_count = nowc, nowsc
            elif nowc == count:
                single_count = max(single_count, nowsc)

        dp[i] = [count, single_count]

    return dp[target]


for t in range(TC):
    answer = solution(target[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
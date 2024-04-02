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


def solution(target):
    
    single = set()
    double = set()
    
    for i in range(1, 21):
        single.add(i)
        double.add(i*2)
        double.add(i*3)
    
    single.add(50)
    
    dp = [[target, 0] for _ in range(target+1)]
    for i in range(1, target+1):
        if i in single:
            dp[i] = [1, 1]
        elif i in double:
            dp[i] = [1, 0]
        else:
            for j in range(i-1, max(0, i-61), -1):
                
                if j in single:
                    now = [dp[i-j][0]+1, dp[i-j][1]+1]    
                elif j in double:
                    now = [dp[i-j][0]+1, dp[i-j][1]]
                else:
                    now = [dp[i-j][0] + dp[j][0], dp[i-j][1] + dp[j][1]]
                
                if now[0] < dp[i][0]:
                    dp[i] = now
                elif now[0] == dp[i][0]:
                    dp[i][1] = max(dp[i][1], now[1])
                
    answer = dp[target]
    return answer


for t in range(TC):
    answer = solution(target[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
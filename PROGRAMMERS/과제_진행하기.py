'''TC1'''
plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
result = ["korean", "english", "math"]
'''TC2'''
plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
result = ["science", "history", "computer", "music"]
'''TC3'''
plans = [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]
result = ["bbb", "ccc", "aaa"]


TC = 3
plans = [[["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]], [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]], [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]]
result = [["korean", "english", "math"], ["science", "history", "computer", "music"], ["bbb", "ccc", "aaa"]]


def solution(plans):


    def strtosec(string):
        return int(string[:2]) * 60 + int(string[3:])


    plans.sort(key = lambda x : (int(x[1][:2]), int(x[1][3:])))
    
    finish = []
    temp = []

    now = plans[0]
    now[1] = strtosec(now[1])
    now[2] = int(now[2])

    for i in range(1, len(plans)):
        name, start, time = plans[i]
        start = strtosec(start)
        time = int(time)
        while now[1] < start:

            if now[1]+now[2] > start:
                temp.append([now[0], now[1]+now[2]-start])
                now[1] = start
            elif now[1]+now[2] == start:
                finish.append(now[0])
                break
            else:
                finish.append(now[0])
                if temp:
                    new = temp.pop()
                    now = [new[0], now[1]+now[2], new[1]]
                else:
                    break
        now = [name, start, time]

    finish.append(now[0])
    for i in range(len(temp)-1, -1, -1):
        finish.append(temp[i][0])
    
    return finish


for t in range(TC):
    answer = solution(plans[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
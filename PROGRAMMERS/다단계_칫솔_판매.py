'''TC1'''
enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
result = [360, 958, 108, 0, 450, 18, 180, 1080]
'''TC2'''
enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["sam", "emily", "jaimie", "edward"]
amount = [2, 3, 5, 4]
result = [0, 110, 378, 180, 270, 450, 0, 0]


TC = 2
enroll = [["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]]
referral = [["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]]
seller = [["young", "john", "tod", "emily", "mary"], ["sam", "emily", "jaimie", "edward"]]
amount = [[12, 4, 2, 5, 10], [2, 3, 5, 4]]
result = [[360, 958, 108, 0, 450, 18, 180, 1080], [0, 110, 378, 180, 270, 450, 0, 0]]


def solution(enroll, referral, seller, amount):
    
    mem_idx = {'-': len(enroll)}

    for i in range(len(enroll)):
        mem_idx[enroll[i]] = i
        referral[i] = mem_idx[referral[i]]

    answer = [0] * len(enroll)
    for i in range(len(seller)):
        s = mem_idx[seller[i]]
        a = amount[i] * 100

        while a > 0:
            answer[s] += a - int(a/10)
            s = referral[s]
            if s == len(enroll): break
            a = int(a/10)
    
    return answer


for t in range(TC):
    answer = solution(enroll[t], referral[t], seller[t], amount[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
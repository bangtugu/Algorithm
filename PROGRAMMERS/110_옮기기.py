'''TC1'''
s = ["1110","100111100","0111111010"]
result = ["1101","100110110","0110110111"]


TC = 1
s = [["1110","100111100","0111111010"]]
result = [["1101","100110110","0110110111"]]


def solution(s):
    
    answer = []
    for string in s:
        temp = ''

        cnt1 = 0
        cnt110 = 0
        for i in range(len(string)):
            if string[i] == '1':
                cnt1 += 1
            elif string[i] == '0':
                if cnt1 >= 2:
                    cnt110 += 1
                    cnt1 -= 2
                else:
                    temp += cnt1*'1'+'0'
                    cnt1 = 0

        temp = temp + cnt110*'110' + cnt1*'1'

        answer.append(temp)
    
    return answer


for t in range(TC):
    answer = solution(s[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
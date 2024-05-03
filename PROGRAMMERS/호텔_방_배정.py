'''TC1'''
k = 10
room_number = [1,3,4,1,3,1]
result = [1,3,4,2,5,6]


TC = 2
k = [10, 1000000000000-1]
room_number = [[1,3,4,1,3,1], [1, 2, 3, 4, 5]]
result = [[1,3,4,2,5,6], [1, 2, 3, 4, 5]]


def solution(k, room_number):
    
    sett = set()
    check_dic = {}
    answer = [0]*len(room_number)
    for i in range(len(room_number)):
        n = room_number[i]-1
        
        while n in sett:
            new = n + check_dic[n]
            check_dic[n] += 1
            if new in sett:
                check_dic[n] += check_dic[new]
            n = new

        answer[i] = n+1
        sett.add(n)
        check_dic[n] = 1

    return answer


for t in range(TC):
    answer = solution(k[t], room_number[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
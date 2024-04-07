'''TC1'''
book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
result = 3
'''TC2'''
book_time = [["09:10", "10:10"], ["10:20", "12:20"]]
result = 1
'''TC3'''
book_time = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
result = 3


TC = 3
book_time = [[["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]], [["09:10", "10:10"], ["10:20", "12:20"]], [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]]
result = [3, 1, 3]


def solution(book_time):
    

    def time(str):
        return int(str[:2])*60 + int(str[3:])


    for i in range(len(book_time)):
        book_time[i] = [time(book_time[i][0]), time(book_time[i][1])]
    
    book_time.sort(key = lambda x : x[0])
    
    e_lst = []
    answer = 0
    for i in range(len(book_time)):
        s, e = book_time[i]
        if not e_lst:
            e_lst = [e+10]
        else:
            for j in range(len(e_lst)):
                if e_lst[j] > s:
                    e_lst = e_lst[j:]
                    e_lst.append(e+10)
                    break
            else:
                e_lst = [e+10]

            e_lst.sort()

        answer = max(answer, len(e_lst))

    
    return answer 


for t in range(TC):
    answer = solution(book_time[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
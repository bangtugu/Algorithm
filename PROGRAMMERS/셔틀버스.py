'''TC1'''
n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
answer = "09:00"
'''TC2'''
n = 2
t = 10
m = 2
timetable = ["09:10", "09:09", "08:00"]
answer = "09:09"
'''TC3'''
n = 2
t = 1
m = 2
timetable = ["09:00", "09:00", "09:00", "09:00"]
answer = "08:59"
'''TC4'''
n = 1
t = 1
m = 5
timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
answer = "00:00"
'''TC5'''
n = 1
t = 1
m = 1
timetable = ["23:59"]
answer = "09:00"
'''TC6'''
n = 10
t = 60
m = 45
timetable = ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
answer = "18:00"


TC = 6
n = [1, 2, 2, 1, 1, 10]
t = [1, 10, 1, 1, 1, 60]
m = [5, 2, 2, 5, 1, 45]
timetable = [["08:00", "08:01", "08:02", "08:03"], ["09:10", "09:09", "08:00"], ["09:00", "09:00", "09:00", "09:00"], ["00:01", "00:01", "00:01", "00:01", "00:01"], ["23:59"], ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]]
result = ["09:00", "09:09", "08:59", "00:00", "09:00", "18:00"]


def solution(n, t, m, timetable):
    

    def get_time(string):
        return int(string[:2])*60 + int(string[3:])
    def get_string(num):
        string1 = str(num//60)
        if len(string1) == 1: string1 = '0' + string1
        string2 = str(num%60)
        if len(string2) == 1: string2 = '0' + string2
        return string1 + ':' + string2
    
    
    for i in range(len(timetable)):
        timetable[i] = get_time(timetable[i])
    timetable.sort()

    start = 9*60
    shuttle = [start + i*t for i in range(n)]
    check = [[] for _ in range(len(shuttle))]
    i, j = 0, 0
    while i < len(shuttle):
        now = shuttle[i]
        while j < len(timetable):
            if timetable[j] > now: break
            check[i].append(timetable[j])
            j += 1
            if len(check[i]) == m: break
        
        if len(check[i]) == m:
            check[i] = max(check[i])-1
        else:
            check[i] = shuttle[i]

        i += 1

    return get_string(max(check))


for T in range(TC):
    answer = solution(n[T], t[T], m[T], timetable[T])
    correct = True if answer == result[T] else False
    comment = "answer = {}".format(result[T]) if correct else "answer = {} your are {}".format(result[T], answer)
    print("TC{} : {} {}".format(T+1, "PASS" if correct else "FAIL", comment))
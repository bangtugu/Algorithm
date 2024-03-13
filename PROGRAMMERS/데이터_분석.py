'''TC1'''
data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"
result = [[3,20300401,10,8],[1,20300104,100,80]]


TC = 1
data = [[[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]]
ext = ["date"]
val_ext = [20300501]
sort_by = ["remain"]
result = [[[3,20300401,10,8],[1,20300104,100,80]]]


def solution(data, ext, val_ext, sort_by):
    word_dic = {
        "code" : 0,
        "date" : 1,
        "maximum" : 2,
        "remain" : 3
    }
    ext = word_dic[ext]
    sort_by = word_dic[sort_by]
    
    answer = []
    for i in range(len(data)):
        if data[i][ext] < val_ext:
            answer.append(data[i])
    
    answer.sort(key = lambda x: x[sort_by])

    return answer


for t in range(TC):
    answer = solution(data[t], ext[t], val_ext[t], sort_by[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, correct, comment))
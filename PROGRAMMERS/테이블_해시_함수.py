'''TC1'''
data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
col = 2
row_begin = 2
row_end = 3
result = 4


TC = 1
data = [[[2,2,6],[1,5,10],[4,2,9],[3,8,3]]]
col = [2]
row_begin = [2]
row_end = [3]
result = [4]


def solution(data, col, row_begin, row_end):
    
    data.sort(key = lambda x : (x[col-1], -x[0]))

    answer = 0
    for i in range(row_begin-1, row_end):
        temp = 0
        for n in data[i]:
            temp += n%(i+1)
        
        answer = answer ^ temp

    return answer


for t in range(TC):
    answer = solution(data[t], col[t], row_begin[t], row_end[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
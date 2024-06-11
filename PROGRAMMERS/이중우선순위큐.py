'''TC1'''
operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
result = [0,0]
'''TC2'''
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
result = [333, -45]


TC = 2
operations = [["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"], ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]]
result = [[0,0], [333, -45]]


def solution(operations):
    
    cnt = 0
    min_Q = []
    max_Q = []

    for line in operations:
        command, num = input().split()
        num = int(num)

        if command == 'I':
            

        if num == 1:


    return


for t in range(TC):
    answer = solution(operations[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
'''TC1'''
N = 5
number = 12
result = 4
'''TC2'''
N = 2
number = 11
result = 3


TC = 6
N = [5, 2, 5, 1, 5, 5]
number = [12, 11, 3125, 121, 3025, 5]
result = [4, 3, 5, 4, 4, 1]


def solution(N, number):
    
    setdic = {0: set()}
    lstdic = {0: []}
    for i in range(1, 9):

        lstdic[i] = []
        setdic[i] = set()
        
        lstdic[i].append(int(str(N)*i))
        setdic[i].add(int(str(N)*i))

        temp = []
        
        for num in lstdic[i-1]:
            temp.append(num+N)
            temp.append(num*N)
            if num >= N: temp.append(num-N)
            if not num % N: temp.append(num//N)

        for j in range(1, i+1):
            z = i - j
            if z < j: continue
            for num1 in lstdic[j]:
                for num2 in lstdic[z]:
                    temp.append(num1+num2)
                    temp.append(num1*num2)
                    temp.append(num1-num2 if num1-num2 >= 0 else num2-num1)
                    if num2 and not num1 % num2: temp.append(num1 % num2)
                    if num1 and not num2 % num1: temp.append(num2 % num1)

        for num in temp:
            if num in setdic[i]: continue
            setdic[i].add(num)
            lstdic[i].append(num)
        
        if number in setdic[i]: return i

    return -1


for t in range(TC):
    answer = solution(N[t], number[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
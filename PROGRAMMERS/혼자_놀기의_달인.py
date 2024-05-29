'''TC1'''
cards = [8,6,3,7,2,5,1,4]
result = 12


TC = 1
cards = [[8,6,3,7,2,5,1,4]]
result = [12]


def solution(cards):
    
    


    return


for t in range(TC):
    answer = solution(cards[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
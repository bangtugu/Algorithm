'''TC1'''
cards = [8,6,3,7,2,5,1,4]
result = 12


TC = 1
cards = [[8,6,3,7,2,5,1,4]]
result = [12]


def solution(cards):
    
    group = []
    check = [0]*len(cards)
    for i in range(len(cards)):
        if check[i]: continue

        cnt = 1
        now = cards[i]-1
        while now != i:
            check[now] = 1
            now = cards[now]-1
            cnt += 1
        group.append(cnt)

    if len(group) <= 1: return 0

    group.sort(reverse=True)
    return group[0]*group[1]


for t in range(TC):
    answer = solution(cards[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
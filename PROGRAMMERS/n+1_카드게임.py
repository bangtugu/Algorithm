'''TC1'''
coin = 4
cards = [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]
result = 5
'''TC2'''
coin = 3
cards = [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]
result = 2
'''TC3'''
coin = 2
cards = [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]
result = 4
'''TC4'''
coin = 10
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
result = 1


TC = 4
coin = [4, 3, 2, 10]
cards = [[3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4], [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12], [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]
result = [5, 2, 4, 1]


def solution(coin, cards):
    n = len(cards)
    h = n//3
    temp = [-1]*n
    cost = {}
    for i in range(1, n//2 + 1):
        cost[i] = 0
    
    round = 0
    while round < (n-n//3)//2+1:
        h = n//3 + round*2
        for i in range(h):
            if temp[i] == -1 and n+1 - cards[i] in cards[:h]:
                temp[i] = round    
                if i >= n//3:
                    cost[min(cards[i], cards[cards.index(n+1-cards[i])])] += 1
                temp[cards.index(n+1-cards[i])] = round
                if cards.index(n+1-cards[i]) >= n//3:
                    cost[min(cards[i], cards[cards.index(n+1-cards[i])])] += 1

        round += 1
    
    answer_round = 1
    now_coin = coin
    now_hand = n//3
    release = [0]*n
    while answer_round <= (n-n//3)//2+1:
        now_hand = n//3+answer_round*2
        if now_hand > n:
            return answer_round
        
        min_cost_realese = [3, [1001, 1002]]

        for i in range(now_hand):
            if release[i] or temp[i]==-1 or temp[i] > answer_round: continue
            if cost[min(cards[i], n+1-cards[i])] > now_coin or cost[min(cards[i], n+1-cards[i])] >= min_cost_realese[0]: continue
            min_cost_realese[0] = cost[min(cards[i], n+1-cards[i])]
            min_cost_realese[1][0] = i
            for j in range(i+1, now_hand):
                if cards[j] == n+1-cards[i]:
                    min_cost_realese[1][1] = j
        
        if min_cost_realese[0] == 3:
            return answer_round
        else:
            now_coin -= min_cost_realese[0]
            for i in min_cost_realese[1]:
                release[i] = answer_round

        answer_round += 1

    return answer_round


for t in range(TC):
    answer = solution(coin[t], cards[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
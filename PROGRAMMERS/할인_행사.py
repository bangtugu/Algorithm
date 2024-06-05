'''TC1'''
want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
result = 3
'''TC2'''
want = ["apple"]
number = [10]
discount = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
result = 0


TC = 2
want = [["banana", "apple", "rice", "pork", "pot"], ["apple"]]
number = [[3, 2, 2, 2, 1], [10]]
discount = [["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]]
result = [3, 0]


def solution(want, number, discount):
    
    
    def is_clear(lst):
        for i in range(len(lst)):
            if lst[i] != 0: return False
        return True


    want_set = set()
    want_dic = {}
    for i in range(len(want)):
        want_dic[want[i]] = i
        want_set.add(want[i])

    N = sum(number)
    for i in range(N):
        if discount[i] in want_set: number[want_dic[discount[i]]] -= 1
    
    answer = 1 if is_clear(number) else 0
    for i in range(N, len(discount)):
        if discount[i-N] in want_set: number[want_dic[discount[i-N]]] += 1
        if discount[i] in want_set: number[want_dic[discount[i]]] -= 1
        if is_clear(number): answer += 1

    return answer


for t in range(TC):
    answer = solution(want[t], number[t], discount[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
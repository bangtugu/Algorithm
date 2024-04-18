'''TC1'''
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
result = 2
'''TC2'''
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
result = 2
'''TC3'''
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
result = 3


TC = 3
user_id = [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["frodo", "fradi", "crodo", "abc123", "frodoc"]]
banned_id = [["fr*d*", "abc1**"], ["*rodo", "*rodo", "******"], ["fr*d*", "*rodo", "******", "******"]]
result = [2, 2, 3]


def is_match(u_lst, b_lst):
    m_lst = [[] for _ in range(len(b_lst))]

    for b in range(len(b_lst)):
        for u in range(len(u_lst)):
            if len(b_lst[b]) != len(u_lst[u]): continue
            for s in range(len(b_lst[b])):
                if b_lst[b][s] == '*': continue
                if b_lst[b][s] != u_lst[u][s]: break
            else:
                m_lst[b].append(u)

    return m_lst


def calc(n, lst, check):
    if n >= len(lst):
        string = ''
        for i in range(len(check)):
            string += str(check[i])
        return [string]
    
    str_lst = []

    for number in lst[n]:
        if check[number]: continue
        check[number] = 1
        str_lst.extend(calc(n+1, lst, check))
        check[number] = 0

    return str_lst


def solution(user_id, banned_id):
    match_lst = is_match(user_id, banned_id)
    cases = set(calc(0, match_lst, [0]*len(user_id)))
    return len(cases)


for t in range(TC):
    answer = solution(user_id[t], banned_id[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
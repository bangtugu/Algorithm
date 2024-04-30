'''TC1'''
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
result = ["ICN", "JFK", "HND", "IAD"]
'''TC2'''
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
result = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]


TC = 2
tickets = [[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]], [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]]
result = [["ICN", "JFK", "HND", "IAD"], ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]]


def solution(tickets):
    
    sett = set()
    port_dic = {}
    roc_dic = {}
    cnt = -1
    lst = []

    for i in range(len(tickets)):
        a, b = tickets[i]

        for c in [a, b]:
            if c in sett: continue
            sett.add(c)
            cnt += 1
            roc_dic[c] = cnt
            port_dic[cnt] = c
            lst.append([])

        a = roc_dic[a]
        b = roc_dic[b]
        lst[a].append([b, i])

    for path in lst:
        path.sort(key = lambda x: port_dic[x[0]])
    check = [0]*len(tickets)


    def path_finder(now, path):
        if len(path) == len(tickets):
            return path

        result_path = []
        for b, i in lst[now]:
            if check[i]: continue
            check[i] = 1
            temp = path_finder(b, path+[i])
            check[i] = 0

            if not temp: continue
            if not result_path:
                result_path = temp
                continue

            for j in range(len(path)):
                port1 = tickets[result_path[j]][1]
                port2 = tickets[temp[j]][1]

                if port1 == port2: continue
                port_lst = sorted([port1, port2])
                result_path = result_path if port_lst[0] == port1 else temp

        return result_path
    

    answer = path_finder(roc_dic['ICN'], [])
    answer = ['ICN'] + [tickets[i][1] for i in answer]

    return answer


for t in range(TC):
    answer = solution(tickets[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
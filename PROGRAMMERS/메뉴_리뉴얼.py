# orders, course, result = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4], ["AC", "ACDE", "BCFG", "CDE"]
orders, course, result = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5], ["ACD", "AD", "ADE", "CD", "XYZ"]
# orders, course, result = ["XYZ", "XWY", "WXA"], [2,3,4], ["WX", "XY"]


def make_lst(order, n):
    alps = list(order)
    alps.sort()
    temps = []
    lst = []
    for i in range(len(alps)):
        for j in range(len(temps)):
            now = temps[j] + alps[i]

            if len(now) == n:
                lst.append(now)
            else:
                temps.append(now)

        temps.append(alps[i])

    return lst


def solution(orders, course):

    order_dic = {}

    for c in course:
        order_dic[c] = {}

    for order in orders:
        l = len(order)

        for i in course:
            if l < i: continue

            lst = make_lst(order, i)
            
            for c in lst:
                if c not in order_dic[i].keys(): order_dic[i][c] = 0
                order_dic[i][c] += 1

    answer = []
    for c in course:
        val = order_dic[c].values()
        if not val: continue
        max_val = max(order_dic[c].values())
        if max_val < 2: continue
        for key in order_dic[c].keys():
            if order_dic[c][key] == max_val:
                answer.append(key)

    answer.sort()
    return answer


print(solution(orders, course))
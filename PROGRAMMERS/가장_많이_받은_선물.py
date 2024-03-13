friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
result = 2

friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
result = 4

friends = ["a", "b", "c"]
gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]
result = 0


def solution(friends, gifts):

    cost = [0] * len(friends)
    table = [[0] * len(friends) for _ in range(len(friends))]
    freinds_dic = {}

    for i in range(len(friends)):
        freinds_dic[friends[i]] = i

    for gift in gifts:
        A, B = map(str, gift.split())
        A = freinds_dic[A]
        B = freinds_dic[B]
        table[A][B] += 1
        cost[A] += 1
        cost[B] -= 1
    
    result = [0] * len(friends)

    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if table[i][j] > table[j][i]: result[i] += 1
            elif table[i][j] < table[j][i]: result[j] += 1
            else:
                if cost[i] > cost[j]: result[i] += 1
                elif cost[i] < cost[j]: result[j] += 1

    return max(result)


print(solution(friends, gifts))
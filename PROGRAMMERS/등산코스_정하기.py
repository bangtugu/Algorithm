n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]

# n = 7
# paths = [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]
# gates = [1]
# summits = [2, 3, 4]

# n = 7
# paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
# gates = [3, 7]
# summits = [1, 5]

# n = 5
# paths = [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]]
# gates = [1, 2]
# summits = [5]


def solution(n, paths, gates, summits):

    answer_summit = n + 1
    answer_intensity = 10000001

    table = [[0] * (n + 1) for _ in range(n + 1)]

    for s, e, l in paths:
        table[s][e] = table[e][s] = l

    for gate in gates:
        for summit in summits:
            intensity_lst = [10000001] * (n + 1)

            now = gate

            while now != summit:

                for i in range(len(intensity_lst)):
                    if (table[now][i] and i not in gates and i not in summits) or i == summit:
                        


    return [answer_summit, answer_intensity]
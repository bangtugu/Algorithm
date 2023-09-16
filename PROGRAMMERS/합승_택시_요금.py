# n, s, a, b, fares, result = 6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]], 82
# n, s, a, b, fares, result = 7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]], 14
n, s, a, b, fares, result = 6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]], 18


def solution(n, s, a, b, fares):
    road_lst = [[] for _ in range(n+1)]

    for fare in fares:
        node1, node2, f = fare
        road_lst[node1].append([node2, f])
        road_lst[node2].append([node1, f])

    # sa + sb, 특정 노드 n ns + na + nb 총 n+1개 경우 중 가장 작은 값 찾기
    # s, a, b에서 모든 노드에 대해 최소요금을 다 구해야하는데 시간 괜찮을까? 괜찮넹 ㅎㅎ
    

    def get_min_fee(start):

        min_fee = [100000*n] * (n+1)
        min_fee[start] = 0

        lst = [start]
        
        i = 0
        while i < len(lst):
            now = lst[i]
            for road in road_lst[now]:
                node, fee = road

                if min_fee[now] + fee < min_fee[node]:
                    min_fee[node] = min_fee[now] + fee
                    lst.append(node)

            i += 1

        return min_fee


    s_min_fee = get_min_fee(s)
    a_min_fee = get_min_fee(a)
    b_min_fee = get_min_fee(b)

    return min([s_min_fee[a] + s_min_fee[b]] + [a_min_fee[i] + b_min_fee[i] + s_min_fee[i] for i in range(1, n+1)])


print(solution(n, s, a, b, fares))
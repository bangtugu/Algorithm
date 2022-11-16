'''
order = [4, 3, 1, 2, 5]
result = 2

order = [5, 4, 3, 2, 1]
result = 5

'''

order = [5, 4, 3, 2, 1]
result = 5


# def solution(order):
#     answer = 0
#
#     cont = []
#     i = 1
#     now = 0
#
#     while True:
#
#         if now == len(order):
#             break
#
#         if order[now] == i:
#             answer += 1
#             now += 1
#             i += 1
#         else:
#             if order[now] in cont:
#                 if cont[-1] == order[now]:
#                     now += 1
#                     answer += 1
#                     cont.pop()
#                 else:
#                     break
#             else:
#                 cont.append(i)
#                 i += 1
#
#     return answer


# def solution(order):
#     answer = 1
#
#     for i in range(1, len(order)):
#
#         if order[i] < order[i-1]:
#             for j in range(order[i]+1, order[i-1]):
#                 if j not in order[:i]:
#                     return answer
#
#         answer += 1
#
#     return answer


# def solution(order):
#     answer = 1
#
#     success = [0] * (len(order)+1)
#     success[order[0]] = 1
#
#     i = order[0]
#
#     for j in range(1, len(order)):
#         if order[j] > order[j-1]:
#             i = order[j]
#         elif order[j-1] - order[j] > 1:
#             while i != order[j]:
#                 if not success[i]:
#                     return answer
#                 i -= 1
#
#         success[i] = 1
#         answer += 1
#
#     return answer


# def solution(order):
#     answer = 1
#
#     success = [0] * (len(order)+1)
#     success[order[0]] = 1
#
#     for j in range(1, len(order)):
#         if order[j] + 1 < order[j-1]:
#             if 0 in success[order[j]+1:order[j-1]]:
#                 return answer
#
#         success[order[j]] = 1
#         answer += 1
#
#     return answer


def solution(order):
    answer = 0
    N = len(order)
    i = 1

    container = []

    while i < N+1:

        container.append(i)

        while container[-1] == order[answer]:
            container.pop()
            answer += 1
            if not len(container):
                break

        i += 1

    return answer




print(solution(order))
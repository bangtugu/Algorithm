# import sys
# input = sys.stdin.readline

# N, K, D = map(int, input().split())
# D_lst = [[i, 0] for i in range(N)]
# K_lst = [set() for _ in range(K+1)]

# for i in range(N):
#     M, d = map(int, input().split())
#     M_lst = list(map(int, input().split()))
#     D_lst[i][1] = d
#     for m in M_lst:
#         K_lst[m].add(i)


# def get(s, e):
#     member = set()
#     for i in range(s, e+1):
#         member.add(D_lst[i][0])
    
#     total_algo = set()
#     aleady_algo = set()
#     for i in range(1, K+1):
#         know_member = K_lst[i]&member
#         if know_member:
#             total_algo.add(i)
#             if know_member == member:
#                 aleady_algo.add(i)
    
#     return (len(total_algo)-len(aleady_algo)) * (e-s+1)


# D_lst.sort(key = lambda x: x[1])
# answer = 0
# s, e = 0, 0
# while e < N-1:
#     while e+1 < N and D_lst[e+1][1] - D_lst[s][1] <= D:
#         e += 1
#     answer = max(answer, get(s, e))
#     temp = D_lst[s][1]
#     while D_lst[s][1] == temp:
#         s += 1

# print(answer)

'''
3 3 10
1 20
1
1 10
2
1 0
3

4
'''

import sys
input = sys.stdin.readline

N, K, D = map(int, input().split())
members = []

for i in range(N):
    M, d = map(int, input().split())
    M_lst = list(map(int, input().split()))
    members.append([d, i, M_lst])


def get(dq):
    total_algo = M_lst[dq[0][1]]
    aleady_algo = M_lst[dq[0][1]]
    for v, i in dq:
        total_algo = total_algo|M_lst[i]
        aleady_algo = aleady_algo&M_lst[i]
    
    return (len(total_algo)-len(aleady_algo)) * len(dq)


members.sort()
answer = 0
s, e = 0, -1
K_dic = {k : 0 for k in range(1, K+1)}
while e < N-1:
    while e+1 < N and members[e+1][0] - members[s][0] <= D:
        for k in members[e+1][2]:
            K_dic[k] += 1
        e += 1

    total = 0
    all_known = 0
    for k in range(1, K+1):
        if K_dic[k]:
            total += 1
            if K_dic[k]== e-s+1:
                all_known += 1
    answer = max(answer, (total-all_known)*(e-s+1))

    temp = members[s][0]
    while s <= e and members[s][0] == temp:
        for k in members[s][2]:
            K_dic[k] -= 1
        s += 1

print(answer)
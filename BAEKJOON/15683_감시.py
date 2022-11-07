# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
#
# def cctving(y, x, lst):
#
#     for z in lst:
#
#         ny = y + dy[z]
#         nx = x + dx[z]
#
#         while 0 <= ny < N and 0 <= nx < M and table[ny][nx] != 6:
#             if table[ny][nx] == 0:
#                 table[ny][nx] = '#'
#
#             ny = ny + dy[z]
#             nx = nx + dx[z]
#
#
# def greedy(n, y, x):
#
#     temp = [0, 0, 0, 0]
#
#     for z in range(4):
#
#         ny = y + dy[z]
#         nx = x + dx[z]
#
#         while 0 <= ny < N and 0 <= nx < M and table[ny][nx] != 6:
#             if table[ny][nx] == 0:
#                 temp[z] += 1
#
#             ny = ny + dy[z]
#             nx = nx + dx[z]
#
#     maxlst = []
#     maxval = 0
#
#     if n == 1:
#         maxlst = [temp.index(max(temp))]
#
#     elif n == 2:
#         for i in range(2):
#             if temp[i] + temp[i+2] > maxval:
#                 maxval = temp[i] + temp[i+2]
#                 maxlst = [i, i+2]
#
#     elif n == 3:
#         for i in range(4):
#             if temp[i] + temp[(i+1)%4] > maxval:
#                 maxval = temp[i] + temp[(i+1)%4]
#                 maxlst = [i, (i+1)%4]
#
#     else:
#         maxlst = [0, 1, 2, 3]
#         maxlst.pop(temp.index(min(temp)))
#
#     cctving(y, x, maxlst)
#
#
# N, M = map(int, input().split())
# table = [list(map(int, input().split())) for _ in range(N)]
#
# cctv_dic = {
#     1: [],
#     2: [],
#     3: [],
#     4: [],
#     5: []
# }
#
# for i in range(N):
#     for j in range(M):
#         if table[i][j] != 0 and table[i][j] != 6:
#             cctv_dic[table[i][j]].append((i, j))
#
# for i in range(5, 0, -1):
#     for cctv in cctv_dic[i]:
#         if i == 5:
#             cctving(cctv[0], cctv[1], [0, 1, 2, 3])
#         else:
#             greedy(i, cctv[0], cctv[1])
#
# ans = 0
# for line in table:
#     ans += line.count(0)
#
# print(ans)

'''
greedy
fail
'''

from copy import deepcopy

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def cctving(n, lst):

    if n == len(cctvs):

        temp_table = deepcopy(table)

        for cctv in lst:                                # cctv = [y, x, [0, 2, 3]]

            y = cctv[0]
            x = cctv[1]

            d_lst = cctv[2]

            for d in d_lst:

                ny = y + dy[d]
                nx = x + dx[d]

                while 0 <= ny < N and 0 <= nx < M and temp_table[ny][nx] != 6:
                    if temp_table[ny][nx] == 0:
                        temp_table[ny][nx] = '#'

                    ny = ny + dy[d]
                    nx = nx + dx[d]

        now_ans = 0
        for line in temp_table:
            now_ans += line.count(0)
        global ans
        ans = min(ans, now_ans)

        return

    d = cctvs[n][0]
    y = cctvs[n][1]
    x = cctvs[n][2]

    if d == 1:
        for i in range(4):
            cctving(n+1, lst + [(y, x, [i])])
    elif d == 2:
        for i in range(2):
            cctving(n+1, lst + [(y, x, [i, i+2])])
    elif d == 3:
        for i in range(4):
            cctving(n+1, lst + [(y, x, [i, (i+1)%4])])
    elif d == 4:
        for i in range(4):
            add_lst = [0, 1, 2, 3]
            add_lst.pop(i)
            cctving(n+1, lst + [(y, x, add_lst)])


N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

cctv_dic = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: []
}

cctvs = []

for i in range(N):
    for j in range(M):
        if table[i][j] != 0 and table[i][j] != 6:                       # 카메라 종류에 따라 cctv_dic에 좌표 저장
            cctv_dic[table[i][j]].append((i, j))

for i in range(5, 0, -1):
    for cctv in cctv_dic[i]:
        if i == 5:                                                      # 5번 카메라는 4방향이니까 미리 진행
            for j in range(4):

                ny = cctv[0] + dy[j]
                nx = cctv[1] + dx[j]

                while 0 <= ny < N and 0 <= nx < M and table[ny][nx] != 6:
                    if table[ny][nx] == 0:
                        table[ny][nx] = '#'

                    ny = ny + dy[j]
                    nx = nx + dx[j]
        else:
            cctvs.append([i, cctv[0], cctv[1]])                         # 카메라 종류, 좌표 저장

ans = N*M                                                               # 최소값 초기화
cctving(0, [])

print(ans)
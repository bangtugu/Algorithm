'''
legacy
'''

# dy = [-1, 1, 0, 0]
# dx = [0, 0, 1, -1]
# d_change = [1, 0, 3, 2]

# R, C, M = map(int, input().split())

# # r, c, s, d, z / y, x, 속력, 방향, 크기
# sharks = []

# for _ in range(M):
#     r, c, s, d, z = map(int, input().split())
#     sharks.append([r-1, c-1, s, d-1, z])

# ans = 0
# p = 1
# while p < C+1:

#     # print(sharks)

#     g_index = -1
#     g_d = R*2

#     for i in range(len(sharks)):
#         if sharks[i][1] == p:
#             if sharks[i][0] < g_d:
#                 g_index = i
#                 g_d = sharks[i][0]

#     if g_index != -1:
#         ans += sharks[g_index][4]
#         # print('ans = {}'.format(ans))
#         sharks.pop(g_index)

#     for i in range(len(sharks)):
#         y = sharks[i][0]
#         x = sharks[i][1]
#         v = sharks[i][2]
#         d = sharks[i][3]

#         while v:

#             if 0 > y+dy[d] or y+dy[d] >= R or 0 > x+dx[d] or x+dx[d] >= C:
#                 d = d_change[d]

#             y += dy[d]
#             x += dx[d]

#             v -= 1

#         sharks[i][0] = y
#         sharks[i][1] = x
#         sharks[i][3] = d

#     sharks.sort(key = lambda x: (x[0], x[1], x[4]))

#     # print(p)
#     # print(sharks)

#     i = 0
#     while i < len(sharks)-1:

#         if sharks[i][0] == sharks[i+1][0] and sharks[i][1] == sharks[i+1][1]:
#             sharks.pop(i)
#             i -= 1
#         i += 1

#     p += 1

# print(ans)


import sys
input = sys.stdin.readline


R, C, M = map(int, input().split())
pool = [[0]*C for _ in range(R)]
start = [list(map(int, input().split())) for _ in range(M)]

for r, c, s, d, z in start:
    pool[r-1][c-1] = [s, d-1, z]

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
answer = 0
for z in range(C):

    for i in range(R):
        if pool[i][z]:
            answer += pool[i][z][2]
            pool[i][z] = 0
            break
    
    lst = []
    for i in range(R):
        for j in range(C):
            if pool[i][j]:
                lst.append([i, j]+pool[i][j])
                pool[i][j] = 0
    
    for r, c, s, d, z in lst:

        nr = r + dr[d]*s
        nc = c + dc[d]*s

        while nr < 0 or nr >= R:
            d = 0 if d else 1
            if nr < 0:
                nr *= (-1)
            else:
                nr = 2*(R-1) - nr
        
        while nc < 0 or nc >= C:
            d = 2 if d == 3 else 3
            if nc < 0:
                nc *= (-1)
            else:
                nc = 2*(C-1) - nc

        if not pool[nr][nc] or pool[nr][nc][2] < z:
            pool[nr][nc] = [s, d, z]

print(answer)
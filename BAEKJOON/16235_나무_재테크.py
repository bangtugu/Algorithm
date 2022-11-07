# def spring():
#
#     trees_g = trees.keys()
#
#     trees_g.sort()
#
#     will_growth = []
#
#     for g in trees_g:
#         for tree in trees[g]:
#             if farm[tree[0]][tree[1]] >= g:
#                 farm[tree[0]][tree[1]] -= g
#                 will_growth.append((g, tree))
#             else:
#                 tree[2] = 0
#
#     for tree in will_growth:
#         if tree[0]+1 in trees.keys():
#             trees[tree[0]+1].append(tree[1])
#         else:
#             trees[tree[0]+1] = [tree[1]]
#         trees[tree[0]].remove(tree[1])
#
#
# def summer():
#
#     will_remove = []
#
#     for g in trees.keys():
#         for tree in trees[g]:
#             if not tree[2]:
#                 farm[tree[0]][tree[1]] += g//2
#                 will_remove.append((g, tree))
#
#     for tree in will_remove:
#         trees[tree[0]].remove(tree[1])
#
#
# def fall():
#
#     for g in range(max(trees.keys())+1):
#         if not g % 5 and g in trees.keys():
#             for tree in trees[g]:
#
#                 y = tree[0]
#                 x = tree[1]
#
#                 for i in range(8):
#
#                     ny = y + dy[i]
#                     nx = x + dx[i]
#
#                     if 0 <= ny < N and 0 <= nx < N:
#                         if 1 in trees.keys():
#                             trees[1].append([ny, nx, 1])
#                         else:
#                             trees[1] = [[ny, nx, 1]]
#
#
# def winter():
#     for i in range(N):
#         for j in range(N):
#             farm[i][j] += feed[i][j]
#
#
# N, M, K = map(int, input().split())
#
# dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# dx = [0, 1, 1, 1, 0, -1, -1, -1]
#
# farm = [[5]*N for _ in range(N)]
#
# feed = [list(map(int, input().split())) for _ in range(N)]
#
# trees = {}
#
# for _ in range(M):
#     x, y, z = map(int, input().split())
#     if z in trees.keys():
#         trees[z].append([y, x, 1])
#     else:
#         trees[z] = [[y, x, 1]]
#
# print(trees)
#
# for i in range(K):
#     spring()
#     summer()
#     fall()
#     winter()
#
# ans = 0
#
# for line in trees:
#     for tree in line:
#         ans += 1
#
# print(ans)

from collections import deque


def spring():

    for i in range(N):
        for j in range(N):
            t_cnt = len(trees[i][j])
            for z in range(t_cnt):
                if farm[i][j] >= trees[i][j][z]:
                    farm[i][j] -= trees[i][j][z]
                    trees[i][j][z] += 1
                else:
                    for _ in range(z, t_cnt):
                        farm[i][j] += trees[i][j].pop() // 2
                    break


def fall():
    for i in range(N):
        for j in range(N):
            farm[i][j] += feed[i][j]
            for tree in trees[i][j]:
                if not tree % 5:

                    for z in range(8):

                        ny = i + dy[z]
                        nx = j + dx[z]

                        if 0 <= ny < N and 0 <= nx < N:
                            trees[ny][nx].appendleft(1)


N, M, K = map(int, input().split())

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

farm = [[5]*N for _ in range(N)]

feed = [list(map(int, input().split())) for _ in range(N)]

trees = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    trees[y-1][x-1].append(z)

for i in range(K):
    spring()
    fall()

ans = 0

for line in trees:
    for spot in line:
        ans += len(spot)

print(ans)
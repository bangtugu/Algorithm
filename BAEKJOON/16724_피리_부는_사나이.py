import sys
input = sys.stdin.readline
# sys.setrecursionlimit(1000) # 재귀시 사용


# N, M = map(int, input().split())
# table = [input() for _ in range(N)]
# check = [[0]*M for _ in range(N)]
# dxy = {
#     'U': [-1, 0],
#     'D': [1, 0],
#     'L': [0, -1],
#     'R': [0, 1]
# }

# cnt_check = [0]
# cnt = 0
# for i in range(N):
#     for j in range(M):
#         if check[i][j]: continue
#         cnt += 1
#         cnt_check.append(1)

#         now = cnt
#         idx = 0
#         lst = [[i, j]]

#         while idx < len(lst):
#             y, x = lst[idx]
#             ny, nx = y + dxy[table[y][x]][0], x + dxy[table[y][x]][1]
#             if not check[ny][nx]:
#                 lst.append([ny, nx])
#                 check[ny][nx] = now
#             elif check[ny][nx] != check[y][x]:
#                 cnt_check[now] = 0
            
#             idx += 1

# print(sum(cnt_check))


N, M = map(int, input().split())
table = [input() for _ in range(N)]
check = [[0]*M for _ in range(N)]
dxy = {
    'U': [-1, 0],
    'D': [1, 0],
    'L': [0, -1],
    'R': [0, 1]
}

cnt = 0
group = 0
for i in range(N):
    for j in range(M):
        if check[i][j]: continue
        group += 1
        cnt += 1
        y, x = i, j
        while True:
            ny, nx = y + dxy[table[y][x]][0], x + dxy[table[y][x]][1]
            if not check[ny][nx]:
                check[ny][nx] = group
            else:
                if check[ny][nx] != check[y][x]:
                    cnt -= 1
                break
            y, x = ny, nx

print(cnt)
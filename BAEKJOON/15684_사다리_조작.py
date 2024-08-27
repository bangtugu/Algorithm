# def set_ladder(n, y, x):
#
#     global ans
#
#     if n >= ans:
#         return
#
#     success = True
#
#     for i in range(N):
#
#         line_stack = []
#
#         for j in range(H):
#             if line[j][i]:
#                 line_stack.append(line[j][i])
#                 if len(line_stack) >= 2 and line_stack[-1] == line_stack[-2]:
#                     line_stack = line_stack[:-2]
#
#         if len(line_stack) != 0:
#             success = False
#             break
#
#     if success:
#         ans = min(ans, n)
#         return
#
#     for i in range(y, H):
#         if i != y:
#             x = 0
#         for j in range(x, N-1):
#             if not line[i][j] and not line[i][j+1] and n+1 < ans:
#                 line[i][j] = 1
#                 line[i][j+1] = 2
#                 set_ladder(n+1, i, j)
#                 line[i][j] = 0
#                 line[i][j+1] = 0


# def check():

#     for i in range(N):

#         temp = i
#         for j in range(H):
#             if line[j][temp] == 1:
#                 temp += 1
#             elif line[j][temp] == 2:
#                 temp -= 1
#         if temp != i:
#             return False

#     return True


# def set_ladder(n, y, x):

#     global ans

#     if n >= ans:
#         return

#     if check():
#         ans = min(n, ans)
#         return

#     if n == 3:
#         return

#     for i in range(y, H):
#         if i != y:
#             x = 0
#         for j in range(x, N-1):
#             if not line[i][j] and not line[i][j+1]:
#                 line[i][j] = 1
#                 line[i][j+1] = 2
#                 set_ladder(n+1, i, j+2)
#                 line[i][j] = 0
#                 line[i][j+1] = 0


N, M, H = map(int, input().split())     #  2 ≤ N ≤ 10, 1 ≤ H ≤ 30, 0 ≤ M ≤ (N-1)×H

line = [[0]* (N) for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    line[a-1][b-1] = 1
    line[a-1][b] = 2


def check():
    for s in range(N):
        now = s
        for j in range(H):
            if line[j][now] == 1: now += 1
            elif line[j][now] == 2: now -= 1
        if now != s: return False
    return True


def dfs(y, x, n):
    global answer

    if n >= answer:
        return

    if check():
        answer = min(answer, n)
        return
    
    if n >= 3:
        return
    
    for i in range(y, H):
        for j in range(x if y==i else 0, N-1):
            if line[i][j] or line[i][j+1]: continue
            line[i][j], line[i][j+1] = 1, 2
            dfs(i, j+2, n+1)
            line[i][j], line[i][j+1] = 0, 0


answer = 4
dfs(0, 0, 0)
if answer > 3:
    print(-1)
else:
    print(answer)
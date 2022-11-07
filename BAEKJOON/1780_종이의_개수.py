# 9
# 0 0 0 1 1 1 -1 -1 -1
# 0 0 0 1 1 1 -1 -1 -1
# 0 0 0 1 1 1 -1 -1 -1
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 0 1 -1 0 1 -1 0 1 -1
# 0 -1 1 0 1 -1 0 1 -1
# 0 1 -1 1 0 -1 0 1 -1


def check(y, x, n):
    global answer

    now_num = table[y][x]
    for i in range(y, y + n):
        for j in range(x, x + n):
            if table[i][j] != now_num:
                for z in range(3):
                    for k in range(3):
                        check(y + (k * n//3), x + (z * n//3), n//3)
                return

    # print(now_num)
    answer[now_num] += 1


N = int(input())

table = [list(map(int, input().split())) for _ in range(N)]

answer = {
    0: 0,
    1: 0,
    -1: 0
}

check(0, 0, N)

print(answer[-1])
print(answer[0])
print(answer[1])
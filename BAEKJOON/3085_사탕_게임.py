N = int(input())
candies = [input() for _ in range(N)]


def check(str):
    max_num = 1
    now_num = 1
    for i in range(1, N):
        if str[i] == str[i-1]:
            now_num += 1
        else:
            now_num = 1
            max_num = max([now_num, max_num])

    return max_num


def row(n):

    max_num = 1

    max_num = max([max_num, check(candies[n])])

    dy = [-1, 1]
    y = n

    for x in range(N):
        for i in range(2):
            ny = y + dy[i]

            if 0 <= ny < N and candies[y][x] != candies[ny][x]:
                max_num = max([max_num, check()])

    return caneat


def col(n):

    dx = [-1, 1]

    for i in range(N):
        for j in range(2):


    return caneat


max_candy = 1
for i in range(N):
    max_candy = max([max_candy, row(i), col(i)])
    if max_candy == N:
        break

print(max_candy)


'''
    문자열으로 하든 리스트로 하든 하나하나 건드리면서 하면 시간초과 날거같은데... 어케해야될지 모르겠다
'''
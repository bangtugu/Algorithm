def move1():
    pass


def move2():
    pass


def move3():
    pass


def move4():
    pass


def dfs(n, d, lst):

    if d == 0:
        move1()
    elif d == 1:
        move2()
    elif d == 3:
        move3()
    elif d == 4:
        move4()

    if n < 5:
        if lst not in his:
            for i in range(4):
                dfs(n+1, i)
    else:

        result = 0
        for i in range(N):
            result = max(result, max(lst[i]))

        global maxnum
        if maxnum < result:
            maxnum = result


N = int(input())

table = [list(map(int, input().split())) for _ in range(N)]

his = []
his.append(table)

maxnum = 2

for d in range(4):
    dfs(1, d, table)

print(maxnum)
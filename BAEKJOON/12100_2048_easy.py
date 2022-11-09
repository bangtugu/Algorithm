from copy import deepcopy


def push(line):

    new_line = []

    for number in line:
        if number:
            new_line.append(number)

    i = 0
    while i < len(new_line) - 1:

        if new_line[i] == new_line[i+1]:
            new_line[i] *= 2
            new_line[i+1] = 0
            i += 1
        i += 1

    if 0 in new_line:
        new_line.remove(0)

    new_line += [0] * (N-len(new_line))

    return new_line


def move1(lst):

    for i in range(N):
        new_line = push(reversed(lst[i]))
        lst[i] = list(reversed(new_line))

    return lst


def move2(lst):

    for i in range(N):
        new_line = [lst[x][i] for x in range(N-1, -1, -1)]
        new_line = list(reversed(push(new_line)))
        for x in range(N):
            lst[x][i] = new_line[x]

    return lst


def move3(lst):
    for i in range(N):
        lst[i] = push(lst[i])

    return lst


def move4(lst):
    for i in range(N):
        new_line = [lst[x][i] for x in range(N)]
        new_line = push(new_line)
        for x in range(N):
            lst[x][i] = new_line[x]

    return lst


def dfs(n, d, lst):

    lst = deepcopy(lst)

    if d == 0:
        lst = move1(lst)
    elif d == 1:
        lst = move2(lst)
    elif d == 2:
        lst = move3(lst)
    elif d == 3:
        lst = move4(lst)

    if n < 5:
        for i in range(4):
            dfs(n+1, i, lst)
    else:
        result = 0
        for i in range(N):
            result = max(result, max(lst[i]))

        global maxnum
        if maxnum < result:
            maxnum = result


N = int(input())

table = [list(map(int, input().split())) for _ in range(N)]

maxnum = 2

for d in range(4):
    dfs(0, d, table)

print(maxnum)

'''

dfs 함수로 4**5번 밀어줌
move1~move4 함수에서 1차원 리스트로 push 함수로 보냄
push 함수에서 작업을 마친 후 move로 반환
move에서 push로부터 반환받은대로 수정하고 dfs로 2차원 리스트 반환

5번 밀어진 케이스에서 max값 찾아서 비교 후 변수 수정
틀렸다고 나오는데 미는부분이 어딘가 잘못 만들어진듯?

'''
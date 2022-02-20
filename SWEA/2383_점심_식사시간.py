import sys
sys.stdin = open('2383_input.txt', 'r')


def getstair(n, lst1, lst2):
    if n == len(persons):
        lst1.sort()
        lst2.sort()
        letsgo(lst1, lst2)
        return

    for i in range(2):
        if i:
            getstair(n+1, lst1, lst2 + [persons[n][i]])
        else:
            getstair(n+1, lst1 + [persons[n][i]], lst2)


def letsgo(lst1, lst2):
    global min_time
    lst11 = lst1[:]
    lst22 = lst2[:]

    for i in range(len(lst1)):
        if i > 2 and lst11[i] < lst11[i-3]:
            lst11[i] = lst11[i-3] + stair1
        else:
            lst11[i] += stair1 + 1
        if lst11[i] > min_time:
            return
    for i in range(len(lst22)):
        if i > 2 and lst22[i] < lst22[i-3]:
            lst22[i] = lst22[i-3] + stair2
        else:
            lst22[i] += stair2 + 1
        if lst22[i] > min_time:
            return

    if not lst11:
        lst11.append(0)
    if not lst22:
        lst22.append(0)

    need = max(max(lst11), max(lst22))

    if min_time > need:
        min_time = need


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    persons = []
    stair = []

    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                persons.append([i, j])
            elif table[i][j] in range(2, 11):
                stair.append([i, j, table[i][j]])

    stair1 = stair[0][2]
    stair2 = stair[1][2]

    for i in range(len(persons)):
        goto1 = abs(persons[i][0] - stair[0][0]) + abs(persons[i][1] - stair[0][1])
        goto2 = abs(persons[i][0] - stair[1][0]) + abs(persons[i][1] - stair[1][1])
        persons[i] = [goto1, goto2]

    min_time = 987654321

    getstair(0, [], [])

    print('#{} {}'.format(test_case, min_time))
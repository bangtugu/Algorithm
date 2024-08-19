def calcline(lst):

    temp_lst = []
    temp_dic = {}

    for num in lst:
        if num != 0:
            if num in tuple(temp_dic.keys()):
                temp_dic[num] += 1
            else:
                temp_dic[num] = 1

    exist_num = list(sorted(temp_dic.keys(), key = lambda x : (temp_dic[x], x)))

    for num in exist_num:
        temp_lst.append(num)
        temp_lst.append(temp_dic[num])

    return temp_lst


def calcR():

    temp = []

    for i in range(len(table)):
        temp.append(calcline(table[i]))

    max_len = max(map(len, temp))

    for i in range(len(temp)):
        if len(temp[i]) < max_len:
            temp[i].extend([0] * (max_len - len(temp[i])))

    return(temp)


def calcC():

    temp = []

    for i in range(len(table[0])):
        temp.append(calcline([table[j][i] for j in range(len(table))]))

    max_len = max(map(len, temp))

    new_table = [[0] * len(temp) for _ in range(max_len)]

    for i in range(len(temp)):
        for j in range(len(temp[i])):
            new_table[j][i] = temp[i][j]

    return(new_table)


r, c, k = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(3)]
for i in range(3):
    n1, n2, n3 = map(int, input().split())
    table[i][0] = n1
    table[i][1] = n2
    table[i][2] = n3

cnt = 0
while cnt < 100:

    if len(table) >= c and len(table[0]) >= r and table[r-1][c-1] == k:
        break

    nowc = len(table)
    nowr = len(table[0])

    if nowc >= nowr:
        table = calcR()

    else:
        table = calcC()

    cnt += 1


if cnt >= 100:
    print(-1)
else:
    print(cnt)
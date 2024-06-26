import sys
import copy
input = sys.stdin.readline


def turn_table(lst):
    if lst[2] == 0:
        return

    lt1, lt2 = lst[0]-lst[2]-1, lst[1]-lst[2]-1
    rb1, rb2 = lst[0]+lst[2]-1, lst[1]+lst[2]-1
    lt_num = temp_table[lt1][lt2]
    for i in range(4):
        if i == 3:
            for j in range(lst[2]*2-1):
                temp_table[lt1][rb2-j] = temp_table[lt1][rb2-j-1]
            temp_table[lt1][lt2+1] = lt_num
        else:
            for j in range(lst[2]*2):
                if i == 0:
                    temp_table[lt1+j][lt2] = temp_table[lt1+j+1][lt2]
                elif i == 1:
                    temp_table[rb1][lt2+j] = temp_table[rb1][lt2+j+1]
                else:
                    temp_table[rb1-j][rb2] = temp_table[rb1-j-1][rb2]
    
    new_lst = lst[:]
    new_lst[2] -= 1
    turn_table(new_lst)


def get_cnts(lst):
    if len(lst) == K:
        cnts.append(lst)
    for i in range(K):
        if not v[i]:
            v[i] = 1
            get_cnts(lst+[i])
            v[i] = 0


N, M, K = map(int, input().split())
table = []
turn_val = []
min_cnt = M * N * 100
v = [0]*K
cnts = []

for i in range(N):
    table.append(list(map(int, input().split())))

for i in range(K):
    turn_val.append(list(map(int, input().split())))

get_cnts([])

for cnt in cnts:
    temp_table = copy.deepcopy(table)
    for i in cnt:
        turn_table(turn_val[i])

    for i in range(N):
        min_cnt = min(min_cnt, sum(temp_table[i]))

print(min_cnt)
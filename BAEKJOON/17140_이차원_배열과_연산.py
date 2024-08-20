import sys
input = sys.stdin.readline


def calcr():

    max_lr = 0
    for i in range(lc):

        dic = {}
        for j in range(lr):
            if not table[i][j]: continue
            if table[i][j] not in dic:
                dic[table[i][j]] = 1
            else:
                dic[table[i][j]] += 1
        
        key_lst = sorted(list(dic.keys()), key = lambda x: [dic[x], x])

        for z in range(100):
            if z >= len(key_lst)*2:
                table[i][z] = 0
            elif z%2:
                table[i][z] = dic[key_lst[z//2]]
            else:
                table[i][z] = key_lst[z//2]

        max_lr = max(max_lr, len(key_lst)*2)

    return min(100, max_lr)


def calcc():
    
    max_lc = 0
    for i in range(lr):

        dic = {}
        for j in range(lc):
            if not table[j][i]: continue
            if table[j][i] not in dic:
                dic[table[j][i]] = 1
            else:
                dic[table[j][i]] += 1
        
        key_lst = sorted(list(dic.keys()), key = lambda x: [dic[x], x])

        for z in range(100):
            if z >= len(key_lst)*2:
                table[z][i] = 0
            elif z%2:
                table[z][i] = dic[key_lst[z//2]]
            else:
                table[z][i] = key_lst[z//2]
        
        max_lc = max(max_lc, len(key_lst)*2)

    return min(100, max_lc)


r, c, k = map(int, input().split())
lr = 3
lc = 3
table = [[0]*100 for _ in range(100)]
for i in range(3):
    n1, n2, n3 = map(int, input().split())
    table[i][0] = n1
    table[i][1] = n2
    table[i][2] = n3

cnt = 0
while cnt < 101:

    if table[r-1][c-1] == k:
        break

    if lc >= lr:
        lr = calcr()
    else:
        lc = calcc()

    cnt += 1

if cnt > 100:
    print(-1)
else:
    print(cnt)
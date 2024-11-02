import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
check = list(input().split()[0])
P = int(input())

on = 0
for i in range(N):
    if check[i] == 'Y':
        check[i] = 1
        on += 1
    else: check[i] = 0


def connecting(on):

    cost = 0
    temp = {}

    for i in range(N):
        if check[i]: continue
        if i not in temp: temp[i] = []
        for j in range(N):
            if i == j: continue
            temp[i].append([costs[i][j], j, check[j]])
        temp[i].sort(key = lambda x: [x[0], -x[2]])
    
    while on < P:
        lst = list(temp.keys())
        lst.sort(key = lambda x: [temp[x][0], -temp[x][2]])

        if P-on == 1:
            catch = 1
            
            while catch:
                for key in lst:
                    if temp[key][0][2]:
                        catch = 0
                        cost += temp[key][0][0]
                        break
                
            
        else:


        if temp[lst[0]][0][2]:
            continue

        print(lst)
        print(temp)
        break


    # cost = 0
    # HQ = []
    # for i in range(N):
    #     for j in range(j+1, N):
    #         if check[i] and check[j]: continue
    #         heappush([costs[i][j], i, j])

    # temp = {}
    # while HQ and P < on:
    #     c, a, b = heappop(HQ)
    #     if check[a] and check[b]: continue
    #     if check[a] != check[b]:
    #         cost += c
    #         on += 1
    #         if check[a]: a, b = b, a
    #         if a in temp:
    #             while temp[a] and P < on:
    #                 c2, b2 = heappop(temp[a])
    #                 on += 1
    #                 cost += c2
    #                 check[b2] = 1
    #         check[a] = check[b] = 1
    #     else:
    #         if a not in temp: temp[a] = []
    #         if b not in temp: temp[b] = []
    #         heappush(temp[b], [c, a])
    #         heappush(temp[a], [c, b])




if not on:
    print(-1)
elif on-P >= 0:
    print(0)
else:
    connecting(on)

'''

3
0 10 11
10 0 12
12 13 0
YNN
3

21

'''
import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    cost = list(map(int, input().split()))
    need = [list(map(int, input().split())) for _ in range(K)]
    W = int(input())-1

    check = [0]*N
    set_lst = [set() for _ in range(N)]
    for a, b in need:
        set_lst[b-1].add(a-1)
    
    answer = 0
    building = []
    while True:
        for i in range(N):
            if not check[i] and not set_lst[i]:
                check[i] += 1
                building.append([cost[i], i])
        
        if check[W]:
            if check[W] == 1:
                answer += cost[W]
            break

        if not building:
            break
        building.sort(key = lambda x: -x[0])
        now_cost = building[-1][0]
        l = len(building)
        for i in range(l-1, -1, -1):
            building[i][0] -= now_cost
            if building[i][0] == 0:
                idx = building[i][1]
                check[idx] += 1
                for sett in set_lst:
                    sett.discard(idx)
                building.pop()
        answer += now_cost

    print(answer)

'''
7
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
8 8
10 20 1 5 8 7 1 43
1 2
1 3
2 4
2 5
3 6
5 7
6 7
7 8
7
3 2
1 2 3 
3 2 
2 1 
1
4 3 
5 5 5 5
1 2
1 3
2 3
4
5 10
100000 99999 99997 99994 99990
4 5
3 5
3 4
2 5
2 4
2 3
1 5
1 4
1 3
1 2
4
4 3
1 1 1 1
1 2
3 2
1 4
4
7 8
0 0 0 0 0 0 0
1 2
1 3
2 4
3 4
4 5
4 6
5 7
6 7
7




120
39
6
5
399990
2
0
'''
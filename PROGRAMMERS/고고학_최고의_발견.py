'''TC1'''
clockHands = [[0,3,3,0],[3,2,2,3],[0,3,2,0],[0,3,3,3]]
result = 3

'''TC2'''
clockHands = [
    [0,0,3,0,0],
    [0,2,3,2,0],
    [3,3,0,3,3],
    [0,2,3,2,0],
    [0,0,3,0,0]
]
result = 4

'''TC3'''
clockHands = [
    [0,0,0,0,0],
    [0,3,0,3,0],
    [3,3,1,3,3],
    [0,2,3,2,0],
    [0,0,3,0,0]
]
result = 3

'''TC4'''
clockHands = [[0, 1, 3, 0],
[1, 2, 0, 0],
[3, 0, 2, 2],
[0, 2, 0, 0]]
result : 8

TC = 4
clockHands = [[[0,3,3,0],[3,2,2,3],[0,3,2,0],[0,3,3,3]],[
    [0,0,3,0,0],
    [0,2,3,2,0],
    [3,3,0,3,3],
    [0,2,3,2,0],
    [0,0,3,0,0]
],[
    [0,0,0,0,0],
    [0,3,0,3,0],
    [3,3,1,3,3],
    [0,2,3,2,0],
    [0,0,3,0,0]
],[[0, 1, 3, 0],
[1, 2, 0, 0],
[3, 0, 2, 2],
[0, 2, 0, 0]]]
result = [3, 4, 3, 8]

'''
2
위에서부터 순서대로 회전 횟수를 구한다면, i+1라인 각 시계의 회전횟수 = 바로 위 i라인 시계의 잔여 회전 횟수이다.
이를 이용하여 가장 윗 줄을 회전시킬 수 있는 3**n개의 경우의 수를 통해 회전 횟수를 구한다.
'''
def solution(clockHands):
    
    N = len(clockHands)
    dy = [0, 0, 0, 1]
    dx = [-1, 0, 1, 0]

    
    from copy import deepcopy
    def check(case):
        
        lst = deepcopy(clockHands)
        count = 0
        for i in range(N):
            count += sum(case)
            for j in range(N):
                for d in range(4):
                    ny = i + dy[d]
                    nx = j + dx[d]
                    if ny >= N or nx < 0 or nx >= N: continue
                    lst[ny][nx] = (lst[ny][nx] + case[j]) % 4
            
            for j in range(N):
                case[j] = (4 - lst[i][j]) % 4

        return count if sum(lst[-1]) == 0 else 3*N*N


    def make_case(n, case):
        if n >= N:
            return check(case)
        
        min_turn = 3*N*N
        for i in range(4):
            min_turn = min(min_turn, make_case(n+1, case+[i]))

        return min_turn
    

    answer = make_case(0, [])
    return answer


'''
1 (그리디)
최초상태에서 해당 칸이 돌아가야할 횟수, 인접 칸 중 가장 많이 돌아가야할 횟수 등을 이용해 그리디하게 짜보려했는데 실패함.
정말 단순한 경우에만 성공함.
'''
def solution2(clockHands):
    
    N = len(clockHands)
    dy = [0, 0, 0, 1, -1]
    dx = [0, 1, -1, 0, 0]


    def check(lst):
        for y in range(N):
            for x in range(N):
                if lst[y][x]%4:
                    return False
        return True


    def check_needturn(lst):
        needturn = [[0]*N for _ in range(N)]
        for y in range(N):
            for x in range(N):
                needturn[y][x] = (4 - lst[y][x]) % 4

        return needturn 


    def check_around(lst):
        around_lst = [[0]*N for _ in range(N)]
        max_around_lst = [[0]*N for _ in range(N)]
        for y in range(N):
            for x in range(N):
                flip = 0
                for d in range(5):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    
                    if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
                    flip += 1 if min_turn[ny][nx] else 0
                    max_around_lst[y][x] = max(lst[nx][ny], max_around_lst[y][x])
                around_lst[y][x] = flip

        return around_lst, max_around_lst 
    

    answer = 0
    while not check(clockHands):
        min_turn = check_needturn(clockHands)
        around_v, around_max= check_around(min_turn)
    
        print(answer, end = '\n\n')
        for line in min_turn:
            print(line)
        print()
        for line in around_v:
            print(line)
        print()

        max_lst = []
        max_v = -1
        max_around = -1
        for y in range(N):
            for x in range(N):
                if around_v[y][x] > max_v:
                    max_lst = [[y, x]]
                    max_v = around_v[y][x]
                    max_around = around_max[y][x]
                elif around_v[y][x] == max_v:
                    if max_around == around_max[y][x]:
                        max_lst.append([y, x])
                    elif around_max[y][x] > max_around:
                        max_lst = [[y, x]]
                        max_around = around_max[y][x]
        
        for y, x in max_lst:
            answer += 1
            for d in range(5):
                ny = y + dy[d]
                nx = x + dx[d]
                if ny < 0 or nx < 0 or nx >= N or ny >= N: continue
                clockHands[ny][nx] = (clockHands[ny][nx] + 1) % 4

    return answer


for t in range(TC):
    answer = solution(clockHands[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
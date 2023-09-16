sales, links, result = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]], 44
# sales, links, result = [5, 6, 5, 3, 4], [[2,3], [1,4], [2,5], [1,2]], 6
# sales, links, result = [5, 6, 5, 1, 4], [[2,3], [1,4], [2,5], [1,2]], 5
# sales, links, result = [10, 10, 1, 1], [[3,2], [4,3], [1,4]], 2


'''
팀이 독립되어있다면 최소매출 직원만 뽑으면 됨, 하지만 1번 팀만 있는게 아닌 이상, 모든 팀이 한 명 이상의 인원을 공유함
공유된 인원들은 모두 한 팀의 팀장이며, 상위 팀에 팀원으로 포함되어있음.
1번 팀을 제외한 팀의 팀장을 선택할 경우 상위 팀의 할당량 또한 해결되므로, 최소매출 인원보다 팀장을 보내는게 최선일 수 있음.
즉 각 팀에서 워크숍을 나갈 수 있는 인원은 최소매출인 팀원(팀장포함) or 팀장임.
각 팀의 팀장, 최소매출인원들을 정리한 후, 완전탐색을 실행하면 O(2**N)의 복잡도 가질 것이라 예상.
어떻게하면 빠르게 구할 수 있을까
'''

check_lst = []
min_price = 0
def solution1(sales, links):
    sales = [0] + sales
    team_dic = {}
    belong = [[] for _ in range(len(sales))]
    
    for link in links:
        leader, follower = link
        if leader not in team_dic.keys():
            team_dic[leader] = [leader, follower]
            belong[leader].append(leader)
        else:
            if sales[team_dic[leader][1]] > sales[follower]:
                team_dic[leader][1] = follower
        belong[follower].append(leader)

    team_lst = list(team_dic.keys())

    global check_lst, min_price
    check_lst = [0] * len(sales)
    for team in team_lst:
        check_lst[team] = 1
    min_price = len(sales) * 10000


    def check(n):
        global check_lst, min_price
        if 1 not in check_lst:
            min_price = min(min_price, n)
            return
        for now_team in team_lst:
            if not check_lst[now_team]: continue
            for target in team_dic[now_team]:
                temp_team = []
                for t in belong[target]:
                    if not check_lst[t]: continue
                    temp_team.append(t)
                    check_lst[t] = 0
                check(n+sales[target])
                for t in temp_team:
                    check_lst[t] = 1
        return


    check(0)

    return min_price


'''
예상했던대로 시간초과

워크샵을 갈 수 있는 대상 : 가장 매출이 작은 팀원(팀장포함), 팀장, 하위 팀 팀장
팀장이 아닌 그냥 팀원이면서 매출액이 가장 작지 않은 경우 대상이 될 수 없다.

가장 기초적인 탐욕 알고리즘 : 각 팀에서 최소매출팀원 고르기
이후 필수적이지 않은 인원 (중복된) 처리,
최소매출이 아니지만 팀장급이라서(두 팀 커버) 더 적은 매출 하락을 기대할 수 있는 경우 확인
'''


def solution2(sales, links):
    sales = [0] + sales
    team_lst = [[] for _ in range(len(sales))]
    Ydp = sales[:]
    Ndp = [0] * len(sales)
    
    for link in links:
        a, b = link
        team_lst[a].append(b)


    def check(n):

        if team_lst[n]:
            for t in team_lst[n]:
                check(t)
        else:
            Ydp[n] = sales[n]
            return
        
        Y = [0, 1000001*len(team_lst[n])]
        for t in team_lst[n]:
            if Ydp[t] - Ndp[t] < Y[1]:
                Y = [t, Ydp[t] - Ndp[t]]

        for t in team_lst[n]:
            if t == Y[0]:
                Ndp[n] += Ydp[t]
            else:
                Ndp[n] += min(Ydp[t], Ndp[t])
            Ydp[n] += min(Ydp[t], Ndp[t])


    check(1)

    return min(Ydp[1], Ndp[1])


print(solution2(sales, links))
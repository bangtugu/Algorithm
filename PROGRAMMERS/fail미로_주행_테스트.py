'''TC1'''
n = 3
m = 5
tests = [[2, 3, 2, 1], [1, 0, 4, 0], [0, 4, 1, 0]]
result = 4
'''TC2'''
n = 99999
m = 99999
tests = [[0, 0, 199997, 1]]
result = 9999999999
'''TC3'''
n = 99999
m = 99999
tests = [[50000, 50000, 3, 0]]
result = 9999999975
'''TC4'''
n = 300
m = 100
tests = [[123, 28, 124, 1], [183, 22, 34, 0], [188, 81, 116, 1], [167, 53, 33, 0], [125, 55, 20, 0]]
result = 6535


TC = 4
n = [3, 99999, 99999, 300]
m = [5, 99999, 99999, 100]
tests = [[[2, 3, 2, 1], [1, 0, 4, 0], [0, 4, 1, 0]], [[0, 0, 199997, 1]], [[50000, 50000, 3, 0]], [[123, 28, 124, 1], [183, 22, 34, 0], [188, 81, 116, 1], [167, 53, 33, 0], [125, 55, 20, 0]]]
result = [4, 9999999999, 9999999975, 6535]


def solution(n, m, tests):

    tests.sort(key = lambda x : [-x[3], x[2]])
    print('정렬할 시간 됨?')
    #ㅇㅇ 됨 최대 776ms


    def cross(case1, case2):
        # 겹치는범위, 안겹치는범위 return
        return

    # 범위 바깥도 제외시켜야되는데 흠...


    # 가장 작은 범위의 도착 테스트케이스부터 시작해서 좁혀나가는게 좋을듯

    # 전부 도착X
    if tests[0][2] == 0:
        # 모든 테스트케이스 범위 밖 = 전부 가능한곳
        # d 큰것부터 작은거 -> 
        pass
    
    # 전부 도착
    elif tests[-1][2] == 1:
        # 모든 테스트케이스 겹치는곳 = 가능한곳
        # d 작은거부터 -> 겹치는곳만 구하기
        pass
    
    # 둘다있음
    else:
        # 도착 테스트케이스 - 도착못한 테스트케이스 = 가능한곳
        # 도착 테스트케이스 겹치는곳 다 구하고 실패 테스트케이스 걸러내기
        pass
    


for t in range(TC):
    answer = solution(n[t], m[t], tests[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
'''TC1'''
numbers = "1756"
result = 10
'''TC2'''
numbers = "5123"
result = 8


TC = 2
numbers = ["1756", "5123"]
result = [10, 8]


def solution(numbers):
    

    def num_to_pad(n):
        if n == 0:
            return 3, 1
        n -= 1
        return n//3, n%3


    move = [[1]*10 for _ in range(10)]
    for i in range(10):
        iy, ix = num_to_pad(i)
        for j in range(10):
            if i == j or move[i][j] != 1: continue
            jy, jx = num_to_pad(j)
            ygap = abs(iy-jy) 
            xgap = abs(ix-jx)
            big, small = max(ygap, xgap), min(ygap, xgap)
            v = (big-small)*2 + small*3
            move[i][j] = move[j][i] = v
    

    '''
    1 (그리디)
    '7387878787878787878'와 같이 오른손이 8로 와서 1의 가중치로 78을 연속해야 하는 경우에도 3번으로 간 오른손이 돌아오지 않음. 실패
    '''
    # left = 4
    # right = 6
    # answer = 0
    # same = [False, []]
    # for i in range(len(numbers)):
    #     nextto = int(numbers[i])        

    #     if same[0]:
    #         lton = move[left][nextto]
    #         rton = move[right][nextto]
    #         ston = move[same[1][-1]][nextto]
    #         if ston == min(lton,rton,ston):
    #             same[1].append(nextto)
    #             answer += ston
    #             continue
    #         elif lton < rton:
    #             answer += lton
    #             left = nextto
    #             right = same[1][-1]
    #             same[0] = False
    #             continue
    #         else:
    #             answer += rton
    #             right = nextto
    #             left = same[1][-1]
    #             same[0] = False
    #             continue
        
    #     if nextto == left or nextto == right:
    #         answer += 1
    #         continue

    #     if move[left][nextto] < move[right][nextto]:
    #         answer += move[left][nextto]
    #         left = nextto
    #     elif move[left][nextto] > move[right][nextto]:
    #         answer += move[right][nextto]
    #         right = nextto
    #     else:
    #         same[0] = True
    #         same[1] = [nextto]
    #         answer += move[left][nextto]

    # return answer
            
    '''
    2 (DP)
    dp[i][l][r] i번째 numbers에 도착한 왼손(l) 오른손(r) 위치까지의 가중치 합 저장
    l, r이 같아질 경우를 잘 걸러내기
    '''
    n = len(numbers)
    dp = [[[-1]*10 for _ in range(10)] for _ in range(n)]

    zero = int(numbers[0])
    dp[0][zero][6] = move[4][zero] if zero != 6 else -1
    dp[0][4][zero] = move[6][zero] if zero != 4 else -1

    for i in range(1,n):
        
        now = int(numbers[i])

        for j in range(10):
            for z in range(10):
                if j == z or dp[i-1][j][z] == -1:continue
                if j != now:
                    if dp[i][j][now] == -1:
                        dp[i][j][now] = dp[i-1][j][z] + move[z][now]
                    else:
                        dp[i][j][now] = min(dp[i][j][now], dp[i-1][j][z] + move[z][now])
                if z != now:
                    if dp[i][now][z] == -1:
                        dp[i][now][z] = dp[i-1][j][z] + move[j][now]
                    else:
                        dp[i][now][z] = min(dp[i][now][z], dp[i-1][j][z] + move[j][now])

    answer = 700007
    for i in range(10):
        for j in range(10):
            if dp[-1][i][j] == -1: continue
            answer = min(answer, dp[-1][i][j])

    return answer


for t in range(TC):
    answer = solution(numbers[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
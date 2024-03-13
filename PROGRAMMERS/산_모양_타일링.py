'''TC1'''
n = 4
tops = [1, 1, 0, 1]
result = 149
'''TC2'''
n = 2
tops = [0, 1]
result = 11
'''TC3'''
n = 10
tops = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
result = 7704


TC = 3
n = [4, 2, 10]
tops = [[1, 1, 0, 1], [0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
result = [149, 11, 7704]


def solution(n, tops):
    
    dp = [[0, 0] for _ in range(n)]

    if tops[0]:
        dp[0] = [3, 1]
    else:
        dp[0] = [2, 1]

    for i in range(1, n):
        if tops[i]:
            dp[i] = [(dp[i-1][0]*3 + dp[i-1][1]*2)%10007, (dp[i-1][0] + dp[i-1][1])%10007]
        else:
            dp[i] = [(dp[i-1][0]*2 + dp[i-1][1])%10007, (dp[i-1][0] + dp[i-1][1])%10007]
        
    return sum(dp[n-1])%10007



    # -------------------------2------------------------------
    
    # from sys import setrecursionlimit

    # setrecursionlimit(150000)

    # lst = [[1, 1], [1, 3]]

    # for i in range(2, n+1):
    #     nlst = [lst[i-2][0]+lst[i-1][0], lst[i-2][1]+lst[i-1][1]]
    #     lst.append(nlst)
    

    # def count(top_lst):
    #     bot_lst = [0]
    #     for top in top_lst:
    #         if top:
    #             bot_lst.append(0)
    #         else:
    #             bot_lst[-1] += 1
        
    #     c = 1
    #     for bot in bot_lst:
    #         c *= lst[bot][0] * lst[bot][1]
    #     return c%10007
    

    # def top_tile(num, top_lst):
    #     if num >= n:
    #         return count(top_lst)

    #     if tops[num]:
    #         A = top_tile(num+1, top_lst)
    #         top_lst[num] = 1
    #         B = top_tile(num+1, top_lst)
    #         top_lst[num] = 0
    #         return A+B
        
    #     return top_tile(num+1, top_lst)
        

    # return top_tile(0, [0]*n)%10007

    
    #------------------------------------1-----------------------------------

    # import sys
    # sys.setrecursionlimit(350000)
    # N = 3
    # M = len(tops)
    # lst = [[1]*n for _ in range(2)] + [tops]


    # def mid_check(y, x, check_lst):
    #     if check_lst[y-1][x] == 2 or (x+1 < M and check_lst[y-1][x+1] == 2): return False
    #     return True


    # def top_check(y, x, check_lst):
    #     if check_lst[y-1][x] == 2 or check_lst[y-2][x] == 2: return False
    #     return True


    # def tiling(n, now_lst):

    #     if n >= N*M:
    #         return 1
    #     if n == 0:
    #         A = tiling(n+1, now_lst)
    #         now_lst[0][0] = 2
    #         B = tiling(n+1, now_lst)
    #         now_lst[0][0] = 1
    #         return (A+B) % 10007
        
    #     A = tiling(n+1, now_lst)
    #     y = n//M
    #     x = n%M
    #     if y == 1 and not mid_check(y, x, now_lst): return A
    #     elif y == 2 and (lst[y][x] == 0 or not top_check(y, x, now_lst)): return A
    #     now_lst[y][x] = 2
    #     B = tiling(n+1, now_lst)
    #     now_lst[y][x] = 1
    #     return (A+B) % 10007
    
    # return tiling(0, lst)


for t in range(TC):
    answer = solution(n[t], tops[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
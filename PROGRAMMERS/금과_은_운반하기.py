'''TC1'''
a = 10
b = 10
g = [100]
s = [100]
w = [7]
t = [10]
result = 50
'''TC2'''
a = 90
b = 500
g = [70,70,0]
s = [0,0,500]
w = [100,100,2]
t = [4,8,1]
result = 499


TC = 2
a = [10, 90]
b = [10, 500]
g = [[100], [70,70,0]]
s = [[100], [0,0,500]]
w = [[7], [100,100,2]]
t = [[10], [4,8,1]]
result = [50, 499]


def solution(a, b, g, s, w, t):
    
    N = len(g)
    
    
    def check(n):
        deliver = [[0, 0, 0] for _ in range(N)]
        for i in range(N):
            cnt = (n//t[i])//2 + (n//t[i])%2
            if cnt*w[i] >= g[i]+s[i]:
                deliver[i] = [g[i], s[i], 0]
            else:
                if cnt*w[i] >= max(g[i],s[i]):
                    deliver[i][2] = g[i] + s[i] - cnt*w[i]
                    deliver[i][0] = g[i] - deliver[i][2]
                    deliver[i][1] = s[i] - deliver[i][2]
                elif cnt*w[i] <= min(g[i],s[i]):
                    deliver[i][2] = cnt*w[i]
                else:
                    deliver[i][2] = min(g[i], s[i])
                    if g[i] > s[i]:
                        deliver[i][0] = cnt*w[i]-deliver[i][2]
                    else:
                        deliver[i][1] = cnt*w[i]-deliver[i][2]
        needg = a
        needs = b
        select = 0
        for i in range(N):
            needg -= deliver[i][0]
            needs -= deliver[i][1]
            select += deliver[i][2]
        
        if needg <= 0: needg = 0
        if needs <= 0: needs = 0

        if needg+needs and needg+needs > select: return 1

        return 2


    end = 0
    for i in range(N):
        end = max(end, (g[i]+s[i]//w[i]+1)*2*t[i])
    start = 0
    mid = end // 2
    while True:
        nowcheck = check(mid)
        if nowcheck == 1:
            start = mid+1
        elif nowcheck == 2:
            end = mid
        mid = (start+end)//2
        if start >= end:
            break
    
    return mid


for T in range(TC):
    answer = solution(a[T], b[T], g[T], s[T], w[T], t[T])
    correct = True if answer == result[T] else False
    comment = "answer = {}".format(result[T]) if correct else "answer = {} your are {}".format(result[T], answer)
    print("TC{} : {} {}".format(T+1, "PASS" if correct else "FAIL", comment))
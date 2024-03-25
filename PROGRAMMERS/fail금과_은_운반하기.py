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
    '''코드 들어갈곳'''
    return


for t in range(TC):
    answer = solution(a[t], b[t], g[t], s[t], w[t], t[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
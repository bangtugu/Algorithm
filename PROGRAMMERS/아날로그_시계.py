'''TC1'''
h1 = 0
m1 = 5
s1 = 30
h2 = 0
m2 = 7
s2 = 0
result = 2
'''TC2'''
h1 = 12
m1 = 0
s1 = 0
h2 = 12
m2 = 0
s2 = 30
result = 1
'''TC3'''
h1 = 0
m1 = 6
s1 = 1
h2 = 0
m2 = 6
s2 = 6
result = 0
'''TC4'''
h1 = 11
m1 = 59
s1 = 30
h2 = 12
m2 = 0
s2 = 0
result = 1
'''TC5'''
h1 = 11
m1 = 58
s1 = 59
h2 = 11
m2 = 59
s2 = 0
result = 1
'''TC6'''
h1 = 1
m1 = 5
s1 = 5
h2 = 1
m2 = 5
s2 = 6
result = 2
'''TC7'''
h1 = 0
m1 = 0
s1 = 0
h2 = 23
m2 = 59
s2 = 59
result = 2852


TC = 7
h1 = [0, 12, 0, 11, 11, 1, 0]
m1 = [5, 0, 6, 59, 58, 5, 0]
s1 = [30, 0, 1, 30, 59, 5, 0]
h2 = [0, 12, 0, 12, 11, 1, 23]
m2 = [7, 0, 6, 0, 59, 5, 59]
s2 = [0, 30, 6, 0, 0, 6, 59]
result = [2, 1, 0, 1, 1, 2, 2852]


def solution(h1, m1, s1, h2, m2, s2):
    
    43200
    start = h1*3600 + m1*60 + s1
    end = h2*3600 + m2*60 + s2
    gap = end - start

    def timepass(s, m, h, t):
        ns = s + 720*t
        nm = m + 12*t
        nh = h + t

        ring = 0
        if s < m and ns >= nm:
            ring += 1
        if s < h and ns >= nh:
            ring += 1
        if ns == nm == nh:
            ring = 1
        
        return ns % 43200, nm % 43200, nh % 43200, ring

    s, m, h, answer = timepass(0, 0, 0, start)
    
    answer = 1 if s == m or s == h else 0
    while gap > 0:
        s, m, h, ring = timepass(s, m, h, 1)
        gap -= 1
        answer += ring

    return answer


for t in range(TC):
    answer = solution(h1[t], m1[t], s1[t], h2[t], m2[t], s2[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
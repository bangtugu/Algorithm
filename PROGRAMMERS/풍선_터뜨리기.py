'''TC1'''
a = [9,-1,-5]
result = 3
'''TC2'''
a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
result = 6


TC = 2
a = [[9,-1,-5], [-16,27,65,-2,58,-92,-71,-68,-61,-33]]
result = [3, 6]


def solution(a):

    if len(a) < 3:
        return len(a)

    answer = 2
    left = 0
    right = len(a)-1
    
    while left < right:
        if a[left] > a[right]:
            temp = a[left]
            while temp <= a[left] and left < len(a):
                left += 1
        else:
            temp = a[right]
            while temp <= a[right] and right >= 0:
                right -= 1
        
        if left < right:
            answer += 1

    return answer


for t in range(TC):
    answer = solution(a[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
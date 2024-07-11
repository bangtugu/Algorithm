import sys
input = sys.stdin.readline


# def numtos(num):
#     string = ''
#     while num > 35:
#         if str(num%36) in numbers:
#             string = str(num%36) + string
#         else:
#             string = chr(num%36 + 55) + string
#         num //= 36
#     if str(num%36) in numbers:
#         string = str(num%36) + string
#     else:
#         string = chr(num%36 + 55) + string
    
#     return string


N = int(input())

numbers = set(list('0123456789'))
lst = [[i, [0]*55, 0] for i in range(36)]
for _ in range(N):
    string = input().split()
    string = string[0]
    for i in range(1, len(string)+1):
        now = string[-i]
        if now not in numbers:
            now = ord(now)-55
        else:
            now = int(now)
        lst[now][1][i-1] += 1
        lst[now][2] += 36**(i-1)*(35-now)

lst.sort(key = lambda x: [-x[2]])

K = int(input())
value = 0
i = 0
while i < 36:
    if i < K: lst[i][0] = 35
    for j in range(55):
        for z in range(lst[i][1][j]):
            value += 36**j*lst[i][0]
    i += 1

answer = ''
while value > 35:
    if str(value%36) in numbers:
        answer = str(value%36) + answer
    else:
        answer = chr(value%36 + 55) + answer
    value //= 36
if str(value%36) in numbers:
    answer = str(value%36) + answer
else:
    answer = chr(value%36 + 55) + answer

print(answer)


'''

5
000GOOD
LUCK
AND
HAVE
FUN
7

'''
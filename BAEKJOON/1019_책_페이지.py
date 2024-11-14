import sys
input = sys.stdin.readline

N = input().split()[0]
length = len(N)

point_dic = {}
for i in range(1, length+1):
    point_dic[i] = [0]*10
    if i > 1:
        for j in range(10):
            if not j:
                point_dic[i][j] += point_dic[i-1][j]*10 + (i-1)*9
                if i - 2: point_dic[i][j] += sum(point_dic[i-2])*9
            if j:
                point_dic[i][j] += point_dic[i-1][j]*10 + 10**(i-1)
    else:
        point_dic[i] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]


print(point_dic)
# 45533
answer = [0]*10
cnt = 0
for i in range(length):
    num = int(N[i])
    c = length-1-i

    print(N, i, num, c)
    for j in range(1 if not i else 0, num+1):
        if c:
            for z in range(10):
                answer[z] += point_dic[c][z]
        cnt += int('9'*c) if c else 0
        print(cnt, answer)
        cnt += 1
        if j == num:
            answer[j] += int(N[i+1:])+1 if i < length-1 else 1
            print(answer)
            break
        else:
            answer[j] += 10**c
            if c - 1 >= 0:
                answer[0] += 10**(c-1)



    
print(*answer)
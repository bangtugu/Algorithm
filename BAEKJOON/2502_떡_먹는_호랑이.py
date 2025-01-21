import sys
input = sys.stdin.readline

D, K = map(int, input().split())
day = [[0, 0] for _ in range(D+1)]
day[1] = [1, 0]
day[2] = [0, 1]

for i in range(3, D+1):
    day[i][0] = day[i-1][0] + day[i-2][0]
    day[i][1] = day[i-1][1] + day[i-2][1]

temp = [0, 0]

for i in range(1, D+1):
    temp[0] += day[i][0]
    temp[1] += day[i][1]

for i in range(1, K+1):
    if not (K-temp[0]*i)%temp[1]:
        print(i)
        print((K-temp[0]*i)//temp[1])
        break

import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

AB, CD = [], []
for i in range(N):
    for j in range(N):
        AB.append(lst[i][0]+lst[j][1])
        CD.append(lst[i][2]+lst[j][3])

AB.sort()
CD.sort(reverse = True)

answer = 0
N *= N
i, j = 0, 0
while i < N and j < N:
    sumv = AB[i] + CD[j]

    if sumv == 0:
        abcnt = 1
        cdcnt = 1
        while i + 1 < N and AB[i] == AB[i+1]:
            i += 1
            abcnt += 1
        while j + 1 < N and CD[j] == CD[j+1]:
            j += 1
            cdcnt += 1
        answer += abcnt * cdcnt
        i += 1
        j += 1
    elif sumv < 0:
        i += 1
    else:
        j += 1

print(answer)
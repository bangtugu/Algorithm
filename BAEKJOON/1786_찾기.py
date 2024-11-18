import sys
input = sys.stdin.readline

T = input()[:-1]
P = input()[:-1]

k = [0]*len(P)
j = 0
for i in range(1, len(P)):
    while j > 0 and P[i] != P[j]:
        j = k[j-1]
    if P[j] == P[i]:
        j += 1
        k[i] = j

answer = []
j = 0
for i in range(len(T)):
    while j>0 and T[i] != P[j]:
        j = k[j-1]
    
    if T[i] == P[j]:
        if j == (len(P)-1):
            answer.append(i-len(P)+2)
            j = k[j]
        else:
            j += 1

print(len(answer))
if answer: print(*answer)
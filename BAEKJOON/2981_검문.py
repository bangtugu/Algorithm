import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()

nlst = [lst[i+1]-lst[i] for i in range(N-1)]
for i in range(N-1):
    temp = set()
    for n in range(2, int(nlst[i]**(1/2))+1):
        if not nlst[i]%n:
            temp.add(n)
            temp.add(nlst[i]//n)
    temp.add(nlst[i])
    nlst[i] = temp

answer = nlst[0]
for i in range(1, N-1):
    answer = answer & nlst[i]

print(*sorted(list(answer)))


'''

A = M * a + R
B = M * b + R
C = M * c + R

B - A = M(b - a)
C - B = M(c - b)

'''
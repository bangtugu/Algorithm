import sys
input = sys.stdin.readline
# sys.setrecursionlimit(1000) # 재귀시 사용

'''
7
3
7
5
2
6
1
4
'''

N = int(input())
answer = N
nlst = [int(input()) for _ in range(N)]

while True:
    print(nlst)

    idx = 0
    maxgap = 0
    for i in range(N):
        gap = max(nlst[i], i+1) - min(nlst[i], i+1)
        if gap > maxgap:
            maxgap = gap
            idx = i

    if maxgap == 0:
        break
    
    num = nlst.pop(idx)
    nlst.insert(num-1, num)

for i in range(N):
    for l in range(i):
        pass
    for r in range(i+1, N):
        pass

print(answer)
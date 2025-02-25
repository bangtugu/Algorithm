import sys
input = sys.stdin.readline

minN, maxN = map(int, input().split())
lst = [1]*(maxN+1-minN)

for i in range(2, int(maxN**(1/2))+1):
    now = i**2
    for catch in range(((minN-1)//now+1)*now, maxN+1, now):
        lst[catch-minN] = 0

print(sum(lst))
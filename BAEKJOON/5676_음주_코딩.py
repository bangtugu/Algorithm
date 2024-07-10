import sys
input = sys.stdin.readline

while True:
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    temp = []
    for i in range(N):
        if lst[i] < 0:
            temp.append([i+1, temp[-1][1]+1])
        elif lst[i] == 0:
            temp.append([i+1, 0])
    
    for _ in range(K):
        M, n1, n2 = input().split()
        n1, n2 = int(n1), int(n2)

        l, r = 0, len(temp)
        while l < r:
            m = (l+r)//2
            if temp[m][0] < n1:
                l = m
            elif temp[m][0] > n1:
                r = m-1
            else:
                break

        if M == 'C':
            if (temp[m][1] < 0 and n2 < 0) or temp[m][1] == n2: continue
            
        else:
            pass
        


'''
4 6
-2 6 0 -1
C 1 10
P 1 4
C 3 7
P 2 2
C 4 -5
P 1 4
5 9
1 5 -2 4 3
P 1 2
P 1 5
C 4 -5
P 1 5
P 4 5
C 3 0
P 1 5
C 4 -5
C 4 -5

0+-
+-+-0
'''
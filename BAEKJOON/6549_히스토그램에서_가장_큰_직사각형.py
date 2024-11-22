import sys
input = sys.stdin.readline

while True:
    lst = list(map(int, input().split()))[1:]
    if not lst: break

    answer = 0
    oblongs = []
    for i in range(len(lst)):
        now = lst[i]
        
        if not oblongs or oblongs[-1][1] < now:
            oblongs.append([i, now])
        else:
            while oblongs and oblongs[-1][1] >= now:
                s, h = oblongs.pop()
                answer = max(answer, (i-s)*h)
                temp = s
            oblongs.append([s, now])

    for s, h in oblongs:
        answer = max(answer, (len(lst)-s)*h)
    
    print(answer)



'''
10 2 1 4 5 1 3 3 1 1 1 1
7 2 1 4 5 1 3 3
4 1000 1000 1000 1000
0
'''

'''
8 1 1 1 1 1 1 1 1
8 1 2 3 4 5 6 7 8
8 1 2 3 4 5 6 7 8
8 1 0 1 0 1 0 1 0
8 0 1 0 1 0 1 0 1
7 2 1 4 5 1 3 3
4 1000 1000 1000 1000
5 1000000000 1000000000 1000000000 1000000000 1000000000
5 0 0 0 0 0
7 8 7 1 1 1 9 6
7 9 6 1 1 1 7 6
0
'''
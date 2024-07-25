import sys
input = sys.stdin.readline

T = int(input())
lst = []
max_n = 0
for _ in range(T):
    now = int(input())
    max_n = max(now, max_n)
    lst.append(now)

dp = [0]*(max_n+1)

for i in range(1, max_n+1):
    if i == 1:
        dp[1] = 1
        continue

    dp[i] += dp[i-1]+1+(i-3)//6 if i%2 else dp[i-1]+1+i//6

for i in lst:
    print(dp[i])



'''
1
1

2
1 1
2

3
1 1 1
1 2
3

4
1 1 1 1
1 1 2
2 2
1 3

5
1 1 1 1 1
1 1 1 2
1 2 2
1 1 3
2 3

6
1 1 1 1 1 1
1 1 1 1 2
1 1 2 2
2 2 2
1 1 1 3
3 3 
1 2 3

7
1 1 1 1 1 1 1
1 1 1 1 1 2
1 1 1 2 2 
1 2 2 2
1 1 1 1 3
1 3 3
1 1 2 3
2 2 3

8
1 1 1 1 1 1 1 1
1 1 1 1 1 1 2
1 1 1 1 2 2
1 1 2 2 2
1 1 1 1 1 3
1 1 3 3
1 1 1 2 3
1 2 2 3
2 2 2 2
2 3 3

9
3 3 3
2 2 2 3

10
2 2 2 2 2
2 2 3 3


'''
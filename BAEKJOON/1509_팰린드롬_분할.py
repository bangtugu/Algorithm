import sys
input = sys.stdin.readline
from collections import deque

string = input().split()[0]

lst = [[] for _ in range(len(string))]

for i in range(len(string)):
    if not string[i]: break
    str1 = ''
    str2 = ''
    for j in range(i, len(string)):
        str1 = str1 + string[j]
        str2 = string[j] + str2

        if str1 == str2:
            lst[i].append(j)

dp = [len(string)]*len(string)
Q = deque()
for i in lst[0]:
    dp[i] = 1
    Q.append([i+1, 1])

while Q:
    now, cnt = Q.popleft()
    if now == len(string):
        dp[-1] = cnt
        break
    
    for i in lst[now]:
        if cnt + 1 < dp[i]:
            Q.append([i+1, cnt+1])
            dp[i] = cnt+1

print(dp[-1])
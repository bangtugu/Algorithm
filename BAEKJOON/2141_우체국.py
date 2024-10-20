import sys
input = sys.stdin.readline

N = int(input())
lst = []
people = 0
for _ in range(N):
    x, a = map(int, input().split())
    people += a
    lst.append([x, a])

lst.sort(key = lambda x: x[0])
temp = people
for i in range(N):
    temp -= lst[i][1]
    if temp <= people//2:
        answer = lst[i][0]
        break

print(answer)
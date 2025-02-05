import sys
input = sys.stdin.readline

N, L = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

answer = 0
e = -1

for i in lst:
    if i > e:
        answer += 1
        e = i+L-1

print(answer)
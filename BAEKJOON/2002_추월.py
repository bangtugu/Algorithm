import sys
input = sys.stdin.readline

N = int(input())
dic = {}
for i in range(N):
    dic[input()] = i

lst = [0]*N
for i in range(N):
    lst[i] = dic[input()]

check = set()
answer = 0
now = 0
for i in range(N):
    cnt = 0
    if i in check: continue
    for j in range(now, N):
        check.add(lst[j])
        if i == lst[j]:
            now = j+1
            answer += cnt
            cnt = 0
            break
        cnt += 1

print(answer)
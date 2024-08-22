import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
sett = set(lst)
connect = [[-1, -1] for _ in range(N)]

idx = {}

for i in range(N):
    idx[lst[i]] = i

for i in range(N):
    if not lst[i]%2 and lst[i]//2 in sett:
        connect[i][1] = idx[lst[i]//2]
    if lst[i]*3 in sett:
        connect[i][0] = idx[lst[i]*3]

answer_lst = []

for i in range(N):
    if sum(connect[i]) == -2:
        answer_lst.append(lst[i])
        break

i = 0
while i < len(answer_lst):
    now = answer_lst[i]

    if not now%3 and now//3 in sett:
        answer_lst.append(now//3)
    if now*2 in sett:
        answer_lst.append(now*2)

    i += 1

answer = ''
for i in range(N-1):
    answer += str(answer_lst[i])+' '
answer += str(answer_lst[-1])

print(answer)
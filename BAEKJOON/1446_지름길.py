import sys
input = sys.stdin.readline
# sys.setrecursionlimit(1000) # 재귀시 사용

N, D = map(int, input().split())

lst = []
for i in range(N):
    s, e, d = map(int, input().split())
    v = e - s - d
    if v <= 0 or e > D: continue

    lst.append([s, e, v])

lst.sort(key = lambda x: x[0])

temp = [[0, D]]
for i in range(len(lst)):
    for j in range(len(temp)):
        e, d = temp[j]
        if e > lst[i][0]: continue
        temp.append([lst[i][1], d-lst[i][2]])

answer = D
for e, d in temp:
    answer = min(d, answer)

print(answer)
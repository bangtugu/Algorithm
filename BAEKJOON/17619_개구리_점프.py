import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
group_at = [0]*(N+1)
lst = []
cnt = 1

for i in range(1, N+1):
    x1, x2, y = map(int, input().split())
    lst.append([i, x1, x2])

lst.sort(key = lambda x: [x[1], x[2]])
group_at[lst[0][0]] = cnt
end = lst[0][2]
for i, x1, x2 in lst[1:]:
    if x1 <= end:
        group_at[i] = cnt
        end = max(end, x2)
    else:
        cnt += 1
        group_at[i] = cnt
        end = x2

for _ in range(Q):
    a, b = map(int, input().split())

    print(1 if group_at[a] == group_at[b] else 0)


'''

4 2
1 5 2
3 7 4
7 9 1
10 13 4
1 3
1 4

'''
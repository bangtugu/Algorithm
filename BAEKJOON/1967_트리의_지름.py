import sys
input = sys.stdin.readline

N = int(input())

p_lst = [0]*N
c_lst = [[] for _ in range(N)]
dic = {}

for _ in range(N-1):
    p, c, l = map(int, input().split())
    p -= 1
    c -= 1
    p_lst[c] = p
    c_lst[p].append(c)
    if p in dic: dic[p][c] = l
    else: dic[p] = {c: l}

dist = []
lst = [0]
while lst:
    dist.append(lst)
    temp = []
    for i in lst:
        temp.extend(c_lst[i])
    lst = temp

answer = 0
l_lst = [0]*N

for i in range(len(dist)-1, -1, -1):

    for now in dist[i]:
        p = p_lst[now]
        if now == p: continue
        if l_lst[p]:
            answer = max(answer, l_lst[now] + l_lst[p] + dic[p][now])
            l_lst[p] = max(l_lst[p], l_lst[now] + dic[p][now])
        else:
            l_lst[p] = l_lst[now] + dic[p][now]
            answer = max(answer, l_lst[p])

print(answer)


'''
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
'''
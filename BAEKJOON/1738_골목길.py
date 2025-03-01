import sys
input = sys.stdin.readline

N, M = map(int, input().split())
roads = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    roads[a-1].append((b-1, -c))

temp = ['not']*N
HQ = [(0, 0, '1')]
temp[0] = 0
answer = []
deadly_cycle = False
from heapq import heappush, heappop
from collections import deque


def cycle(lst, start):
    for i in range(len(lst)):
        if lst[i] == start:
            lst = lst[i:]
            break
    check = [0]*N
    for i in range(len(lst)):
        lst[i] -= 1
        check[lst[i]] = 1
    Q = deque(lst)
    while Q:
        now = Q.popleft()
        for next, c in roads[now]:
            if check[next]: continue
            check[next] = 1
            Q.append(next)
    
    if check[N-1]: return True


while HQ:
    if deadly_cycle: break
    c, now, string = heappop(HQ)
    if now == N-1:
        if not answer or c < answer[0]:
            answer = [c] + list(string.split())
    if c > temp[now]: continue

    for next, cost in roads[now]:
        if temp[next] == 'not' or temp[next] > c + cost:
            if str(next+1) in list(string.split()):
                if cycle(list(map(int, string.split())), next+1):
                    deadly_cycle = True
                    break
                continue
            temp[next] = c + cost
            heappush(HQ, (c+cost, next, string+' '+str(next+1)))

if not answer or deadly_cycle: answer = [-1, -1]
print(*answer[1:])
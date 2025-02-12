import sys
input = sys.stdin.readline

N, M = map(int, input().split())

power_check = {}
power_lst = []

for _ in range(N):
    a, b = input().split()
    b = int(b)
    if b in power_check: continue
    power_lst.append(b)
    power_check[b] = a
power_lst.sort()


def find(power):
    s, e = 0, len(power_lst)-1
    now = e
    while s < e:
        m = (s+e)//2
        if power_lst[m] == power:
            return power_check[power_lst[m]]
        elif power_lst[m] > power:
            now = m
            e = m
        else:
            s = m + 1
    
    return power_check[power_lst[now]]
    

user_check = {}
for _ in range(M):
    t = int(input())
    if t in user_check:
        print(user_check[t])
    else:
        medal = find(t)
        print(medal)
        user_check[t] = medal
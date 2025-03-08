import sys
input = sys.stdin.readline

M = int(input())
m_lst = list(map(int, input().split()))
m_c_lst = [[] for _ in range(M)]

for i in range(M):
    if m_c_lst[i]: continue
    now = m_lst[i]
    lst = [now]
    check = set([now])
    now = m_lst[now-1]
    while now not in check:
        lst.append(now)
        check.add(now)
        now = m_lst[now-1]
    
    for j in range(len(lst)):
        m_c_lst[lst[j]-1] = lst[j:] + lst[:j]

Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    while a and not m_c_lst[b-1]:
        b = m_lst[b-1]
        a -= 1
    if m_c_lst[b-1]:
        print(m_c_lst[b-1][a%len(m_c_lst[b-1])])
    else:
        print(b)
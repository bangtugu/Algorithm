import sys
sys.stdin = open('1248_input.txt', 'r')
from collections import deque

T = int(input())

for test_case in range(1, T+1):
    V, E, t1, t2 = map(int, input().split())
    lst = list(map(int, input().split()))

    table = [[] for _ in range(V + 1)]
    reverse_table = [[] for _ in range(V + 1)]

    for i in range(E):
        reverse_table[lst[i*2+1]] = lst[i*2]
        table[lst[i*2]].append(lst[i*2+1])

    p_lst1 = [t1]
    p_lst2 = [t2]

    while t1:
        t1 = reverse_table[t1]
        p_lst1.append(t1)

    while t2:
        t2 = reverse_table[t2]
        p_lst2.append(t2)

    cnt1 = 1
    while p_lst1[-cnt1] == p_lst2[-cnt1]:
        cnt1 += 1

    cnt1-=1

    cnt2 = 0
    Q = deque()
    Q.append(p_lst1[-cnt1])

    while Q:
        now = Q.popleft()
        for num in table[now]:
            Q.append(num)
        cnt2 += 1

    print('#{} {} {}'.format(test_case, p_lst1[-cnt1], cnt2))
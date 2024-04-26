import sys
input = sys.stdin.readline


T = int(input())

for tc in range(T):
    K, N = map(int, input().split())
    lst = []
    while len(lst) < N:
        lst.extend(map(int, input().split()))

    sorted_lst = sorted(lst)

    idx = 0
    for i in range(N):
        if lst[i] == sorted_lst[idx]:
            idx += 1
    
    print(K, N-idx)
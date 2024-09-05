import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):

    N = int(input())
    start = list(map(int, input().split()))
    M = int(input())
    left_cnt = [0]*N
    comparison = [[0]*N for _ in range(N)]

    for i in range(N):
        left_cnt[start[i]-1] = i
        for j in range(i+1, N):
            comparison[start[i]-1][start[j]-1] = 1
    
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if comparison[b][a]:
            a, b = b, a
        comparison[a][b] = 0
        comparison[b][a] = 1
        left_cnt[a] += 1
        left_cnt[b] -= 1
        
    end = [0]*N
    for i in range(N):
        end[left_cnt[i]] = i+1
    
    if 0 in end:
        print('IMPOSSIBLE')
    else:
        print(*end)
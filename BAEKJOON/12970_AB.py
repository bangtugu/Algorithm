import sys
input = sys.stdin.readline


def fun(N, K):
    cnt = int(K**(1/2))
    if not cnt: return 'B'*N
    
    left = K-cnt**2
    lcnt = left//cnt if not left%cnt else left//cnt + 1
    if lcnt+cnt*2 > N: return -1
    
    answer = 'B'*(N-lcnt-cnt*2)
    temp = []

    temp = ['A']*cnt + ['B']*cnt
    temp = ['A']*(left//cnt) + temp
    if left%cnt:
        temp = temp[:-(left%cnt)] + ['A'] + temp[-(left%cnt):]
    
    for a in temp:
        answer += a

    return answer


N, K = map(int, input().split())
print(fun(N, K))
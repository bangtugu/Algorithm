import sys
input = sys.stdin.readline


def get_candy(r, s, e, x):

    if s >= e: return s
    m = (s+e)//2

    if candy[x*2] >= r:
        return get_candy(r, s, m, x*2)
    else:
        return get_candy(r-candy[x*2], m+1, e, x*2+1)


def set_candy(t, n, s, e, x):
    candy[x] += n
    if s >= e: return
    m = (s+e)//2
    if t <= m:
        set_candy(t, n, s, m, x*2)
    else:
        set_candy(t, n, m+1, e, x*2+1)


M = 4*10**6
N = int(input())
candy = [0]*M
for _ in range(N):
    order = list(map(int, input().split()))
    if order[0] == 1:
        answer = get_candy(order[1], 1, 10**6, 1)
        print(answer)
        set_candy(answer, -1, 1, 10**6, 1)
    else:
        set_candy(order[1], order[2], 1, 10**6, 1)
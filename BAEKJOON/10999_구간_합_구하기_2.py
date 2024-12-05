import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
lst = [0] + [int(input()) for _ in range(N)]
tree = [0]*(N*4)
temp = [0]*(N*4)


def init_tree(s, e, x):
    if s >= e:
        tree[x] = lst[s]
        return

    m = (s+e)//2
    init_tree(s, m, x*2)
    init_tree(m+1, e, x*2+1)
    tree[x] = tree[x*2]+tree[x*2+1]


def get_temp(s, e, x):
    if temp[x] == 0: return

    tree[x] += (e-s+1)*temp[x]
    if s != e:
        temp[x*2] += temp[x]
        temp[x*2+1] += temp[x]
    temp[x] = 0


def set_tree(s, e, l, r, x):
    get_temp(s, e, x)

    if e < l or s > r: return
    if l <= s and e <= r:
        tree[x] += (e-s+1)*d
        if s != e:
            temp[x*2] += d
            temp[x*2+1] += d
        return
    
    m = (s+e)//2
    set_tree(s, m, l, r, x*2)
    set_tree(m+1, e, l, r, x*2+1)
    tree[x] = tree[x*2] + tree[x*2+1]


def get_tree(s, e, l, r, d, x):
    get_temp(s, e, x)

    if e < l or s > r: return 0
    if l <= s and e <= r:
        return tree[x]
    
    value = 0
    m = (s+e)//2
    if l <= m:
        value += get_tree(s, m, l, r, d, x*2)
    if r >= m+1:
        value += get_tree(m+1, e, l, r, d, x*2+1)

    return value


init_tree(1, N, 1)
for _ in range(M+K):
    now = list(map(int, input().split()))

    if len(now) == 3:
        a, b, c = now
        if b > c: b, c = c, b
        print(get_tree(1, N, b, c, 0, 1))
    else:
        a, b, c, d = now
        if b > c: b, c = c, b
        set_tree(1, N, b, c, 1)
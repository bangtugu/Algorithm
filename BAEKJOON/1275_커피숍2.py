import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000)


def creat(l, r, i):
    if l == r:
        tree[i] = lst[l]
        return tree[i]
    
    m = (l+r)//2
    tree[i] += creat(l, m, i*2)
    tree[i] += creat(m+1, r, i*2+1)
    return tree[i]


def get(l, r, i):
    if y < l or x > r: return 0
    if x <= l and r <= y:
        return tree[i]
    
    value = 0
    m = (l+r)//2
    value += get(l, m, i*2)
    value += get(m+1, r, i*2+1)

    return value


def update(l, r, i, t, g):
    if l <= t <= r:
        tree[i] += g
    if l == r: return
    
    m = (l+r)//2
    if l <= t <= m:
        update(l, m, i*2, t, g)
    elif m+1 <= t <= r:
        update(m+1, r, i*2+1, t, g)


N, Q = map(int, input().split())
lst = list(map(int, input().split()))
tree = [0]*((400)**2*2)
creat(0, N-1, 1)

for _ in range(Q):
    x, y, n, a = map(int, input().split())
    x, y, n = x-1, y-1, n-1
    if x > y: x, y = y, x

    print(get(0, N-1, 1))
    update(0, N-1, 1, n, a - lst[n])
    lst[n] = a
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
lst = [0] + [int(input()) for _ in range(N)]
tree = [0]*(N*5)


def init_tree(l, r, n):

    if l >= r:
        tree[n] = lst[l]
        return tree[n]

    m = (l+r)//2
    left = init_tree(l, m, n*2)
    right = init_tree(m+1, r, n*2+1)

    tree[n] = left + right

    return tree[n]


def set_tree(l, r, n):
    if l >= r:
        tree[n] = lst[b]
        return lst[b]
    
    left = tree[n*2]
    right = tree[n*2+1]

    m = (l+r)//2
    if b <= m:
        left = set_tree(l, m, n*2)
    else:
        right = set_tree(m+1, r, n*2+1)

    tree[n] = left + right

    return tree[n]


def get_value(l, r, n):
    
    if l >= b and r <= c:
        return tree[n]
    if c < l or b > r:
        return 1
    
    value = 0
    m = (l+r)//2
    if b <= m:
        value += get_value(l, m, n*2)
    if c > m:
        value += get_value(m+1, r, n*2+1)

    return value


init_tree(1, N, 1)
for i in range(M+K):
    a, b, c = map(int, input().split())

    if a == 1:
        lst[b] = c
        set_tree(1, N, 1)
    if a == 2:
        print(get_value(1, N, 1))
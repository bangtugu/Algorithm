import sys
input = sys.stdin.readline


def get(l, r, i):
    if x <= l and r <= y:
        return tree[i]
    
    m = (l+r)//2
    value = 0
    if x <= m:
        value += get(l, m, i*2)
    if m+1 <= y:
        value += get(m+1, r, i*2+1)
    
    return value


def update(l, r, i):
    tree[i] += g

    if l == r: return

    m = (l+r)//2
    if x <= m:
        update(l, m, i*2)
    else:
        update(m+1, r, i*2+1)


N, M = map(int, input().split())
tree = [0]*(N*4)
lst = [0]*N

for _ in range(M):
    t, x, y = map(int, input().split())

    if t:
        g = y - lst[x-1]
        update(1, N, 1)
        lst[x-1] = y
    else:
        if x > y:
            x, y = y, x
        print(get(1, N, 1))


'''

3 5
0 1 3
1 1 2
1 2 3
0 2 3
0 1 3

'''
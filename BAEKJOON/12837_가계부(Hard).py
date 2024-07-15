import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000)

N, Q = map(int, input().split())
tree = [0] * (N*5)

def update(l, r, i):
    tree[i] += y

    if l == r: return

    m = (l+r)//2
    if l <= x <= m:
        update(l, m, i*2)
    else:
        update(m+1, r, i*2+1)


def get(l, r, i):
    if x <= l and r <= y:
        return tree[i]
    if y < l or x > r: return 0

    value = 0
    m = (l+r)//2
    if x <= m:
        value += get(l, m, i*2)
    if m+1 <= y:
        value += get(m+1, r, i*2+1)

    return value


for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        update(1, N, 1)
    else:
        print(get(1, N, 1))
        





'''

10 6
1 3 10000
1 4 -5000
1 7 -3000
2 1 10
1 6 35000
2 4 10

'''
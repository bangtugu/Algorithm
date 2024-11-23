import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
rlst = []
for _ in range(N):
    num = int(input())
    lst.append(num)
    rlst.append(-num)
max_tree = [0]*(N*4)
min_tree = [0]*(N*4)


def set_tree(tree, lst, s, e, x):

    if s >= e:
        tree[x] = lst[s]
        return tree[x]
    
    m = (s+e)//2

    left = set_tree(tree, lst, s, m, x*2)
    right = set_tree(tree, lst, m+1, e, x*2+1)
    tree[x] = max(left, right)

    return tree[x]


set_tree(max_tree, lst, 0, N-1, 1)
set_tree(min_tree, rlst, 0, N-1, 1)


def get_tree(tree, lst, s, e, x):
    
    if s > r or e < l: return lst[l]
    if l <= s and e <= r: return tree[x]

    m = (s+e)//2

    left = lst[l]
    right = lst[l]
    if l <= m:
        left = get_tree(tree, lst, s, m, x*2)
    if m+1 <= r:
        right = get_tree(tree, lst, m+1, e, x*2+1)
    
    return max(left, right)


for _ in range(M):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(-get_tree(min_tree, rlst, 0, N-1, 1), get_tree(max_tree, lst, 0, N-1, 1))
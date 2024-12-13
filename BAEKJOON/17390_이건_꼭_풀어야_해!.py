# import sys
# input = sys.stdin.readline

# N, Q = map(int, input().split())
# lst = [0] + sorted(list(map(int, input().split())))
# tree = [0]*(N*4)


# def set_tree(s, e, x):
#     if s >= e:
#         tree[x] = lst[s]
#         return
    
#     m = (s+e)//2
#     set_tree(s, m, x*2)
#     set_tree(m+1, e, x*2+1)
#     tree[x] += tree[x*2] + tree[x*2+1]


# def get_tree(s, e, l, r, x):
#     if l <= s and e <= r:
#         return tree[x]

#     if e < l or s > r: return 0

#     m = (s+e)//2
#     left = get_tree(s, m, l, r, x*2)
#     right = get_tree(m+1, e, l, r, x*2+1)

#     return left+right


# set_tree(1, N, 1)
# for _ in range(Q):
#     l, r = map(int, input().split())
#     print(get_tree(1, N, l, r, 1))


import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
lst = [0] + sorted(list(map(int, input().split())))

for i in range(1, N+1):
    lst[i] += lst[i-1]

for _ in range(Q):
    l, r = map(int, input().split())
    print(lst[r]-lst[l-1])
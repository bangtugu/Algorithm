import sys
input = sys.stdin.readline
sys.setrecursionlimit(11000)

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
lst.sort(key = lambda x: x[2])

g = [i for i in range(N+1)]
answer = 0


def leader(n):
    if g[n] != n:
        g[n] = leader(g[n])
    
    return g[n]


for A, B, C in lst:
    a = leader(A)
    b = leader(B)
    if a == b: continue

    answer += C
    if a < b:
        g[b] = a
    else:
        g[a] = b

print(answer)
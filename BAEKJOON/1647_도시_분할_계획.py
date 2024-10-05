import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = [i for i in range(N+1)]
lst = [list(map(int, input().split())) for _ in range(M)]
lst.sort(key = lambda x: x[2])


def leader(n):
    if G[n] != n:
        G[n] = leader(G[n])
    
    return G[n]


cnt = N-2
answer = 0
for a, b, c in lst:
    if not cnt: break
    A = leader(a)
    B = leader(b)
    if A == B: continue

    answer += c
    cnt -= 1
    if A < B:
        G[B] = A
    else:
        G[A] = B

print(answer)
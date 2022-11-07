
# def finddd(n1, n2, n3):
#     global mincnt
#     if n3 >= mincnt:
#         return
#
#     if n1 == n2:
#         mincnt = n3
#         return
#
#     finddd(n1+1, n2, n3+1)
#     finddd(n1*2, n2, n3+1)
#     finddd(n1-1, n2, n3+1)

from collections import deque

N, K = map(int, input().split())

MAX = max(N, K*2)

v = set()

v.add(N)

Q = deque()
Q.append((N, 0))

while Q:
    nowN, nowcnt = Q.popleft()

    if nowN == K:                               # bfs이므로 가장 먼저 K에 도달하면 그게 최소횟수임.
        mincnt = nowcnt
        print(mincnt)
        break

    for newN in (nowN - 1, nowN + 1, nowN * 2): # 3가지 경우 모두에 대해서
        if 0 <= newN <= MAX and newN not in v:  # 이미 방문했던 수가 아니고, 조건 범위 이내의 수일때에만 확인
            v.add(newN)
            Q.append((newN, nowcnt+1))


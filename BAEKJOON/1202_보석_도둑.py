import sys
input = sys.stdin.readline


N, K = map(int, input().split())
import heapq

M_heapq = []
for _ in range(N):
    M, V = map(int, input().split())
    heapq.heappush(M_heapq, [M, V])

bag = [int(input()) for _ in range(K)]
bag.sort()

answer = 0
V_heapq = []
for b in bag:
    while M_heapq and M_heapq[0][0] <= b:
        heapq.heappush(V_heapq, -heapq.heappop(M_heapq)[1])
    
    if V_heapq:
        answer -= heapq.heappop(V_heapq)

print(answer)
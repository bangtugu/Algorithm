import sys
input = sys.stdin.readline
import heapq

N = int(input())

Q = []
answer = 0

for i in range(N):
    new = int(input())
    heapq.heappush(Q, new)

while len(Q) > 1:
    A = heapq.heappop(Q)
    B = heapq.heappop(Q)
    heapq.heappush(Q, A+B)
    answer += A+B

print(answer)
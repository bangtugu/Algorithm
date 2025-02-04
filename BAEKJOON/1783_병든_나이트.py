import sys
input = sys.stdin.readline

N, M = map(int, input().split())
if N == 1:
    answer = 1
elif N == 2:
    answer = min(4, (M-1)//2 + 1)
elif M < 7:
    answer = min(4, M)
else:
    answer = (2 + (M-5)) + 1

print(answer)
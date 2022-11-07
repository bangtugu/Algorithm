import sys

N = int(sys.stdin.readline())

stairs = [0] * N

for i in range(N):
    stairs[i] = int(sys.stdin.readline())

if N == 1:
    print(stairs[0])
elif N == 2:
    print(sum(stairs))
elif N == 3:
    print(max(stairs[1]+stairs[2], stairs[0]+stairs[2]))
else:

    step = [0] * N

    step[0] = stairs[0]
    step[1] = stairs[0] + stairs[1]
    step[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, N):
        step[i] = max(step[i-3] + stairs[i-1] + stairs[i], step[i-2]+stairs[i])

    print(step[N-1])

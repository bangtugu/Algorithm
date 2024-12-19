import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    temp = x
    answer = -1
    while temp <= M*N:
        if not (temp-x)%M and not (temp-y)%N:
            answer = temp
            break
        temp += M
    
    print(answer)
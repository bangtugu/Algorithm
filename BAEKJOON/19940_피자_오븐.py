import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    answer = [0, 0, 0, 0, 0]
    if N % 10 < 5:
        answer[4] += N % 10
        N -= N % 10
    elif N % 10 > 5:
        answer[3] += 10 - (N % 10)
        N += 10 - (N % 10)
    
    

    print(*answer)
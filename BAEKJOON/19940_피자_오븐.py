import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    answer = [0, 0, 0, 0, 0]

    answer[0] += N//60
    N %= 60

    if N % 10 < 5:
        answer[3] += N % 10
        N -= N % 10
    elif N % 10 > 5:
        answer[4] += 10 - (N % 10)
        N += 10 - (N % 10)
    else:
        if N + 5 > 40:
            answer[4] += 5
            N += 5
        else:
            answer[3] += 5
            N -= 5

    
    if N % 60 <= 30:
        answer[1] += (N % 60)//10
        N -= N % 60
    else:
        answer[2] += 6 - (N % 60)//10
        N += 60 - (N % 60)
    
    answer[0] += N//60
    print(*answer)
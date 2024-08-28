import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [input() for _ in range(N)]

Bfirstsum = [[0]*(M+1) for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        Bfirstsum[i][j] = Bfirstsum[i-1][j] + Bfirstsum[i][j-1] - Bfirstsum[i-1][j-1]
        if (i+j)%2 == (board[i][j] != 'W'):
            Bfirstsum[i][j] += 1

answer = K*K
for i in range(K-1, N):
    for j in range(K-1, M):
        now = Bfirstsum[i][j] - Bfirstsum[i-K][j] - Bfirstsum[i][j-K] + Bfirstsum[i-K][j-K]
        answer = min(answer, now, K*K-now)

print(answer)
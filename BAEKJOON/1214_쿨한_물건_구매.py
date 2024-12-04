import sys
input = sys.stdin.readline

D, P, Q = map(int, input().split())

if P < Q: P, Q = Q, P
cnt = min(D//P+1, Q)
answer = 10**10

for i in range(cnt):
    answer = min(answer, (Q-(D-P*i)%Q)%Q)
answer = min(answer, (P-(D%P))%P)

print(answer+D)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

temp = sum(lst[:K])
answer = temp
for i in range(N-K):
    temp = temp-lst[i]+lst[i+K]
    answer = max(answer, temp)
        
print(answer)
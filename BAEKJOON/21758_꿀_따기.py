import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))
all_sum = sum(lst)
sum1 = all_sum - lst[0]
sum2 = all_sum - lst[-1]
answer = 0

for i in range(1, N-1):
    answer = max(answer, all_sum-lst[0]-lst[-1]+lst[i])
    sum1 -= lst[i]
    sum2 -= lst[-(i+1)]
    answer = max(answer, all_sum-lst[0]-lst[i]+sum1)
    answer = max(answer, all_sum-lst[-1]-lst[-(i+1)]+sum2)

print(answer)
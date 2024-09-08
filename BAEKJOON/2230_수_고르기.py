import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num_set = set()
for _ in range(N):
    num = int(input())
    num_set.add(num)

lst = sorted(list(num_set))

answer = lst[-1] - lst[0]
l, r = 0, 0
while l <= r and r < len(lst):
    
    if lst[r] - lst[l] < M:
        r += 1
    else:
        answer = min(answer, lst[r]-lst[l])
        l += 1

print(answer)
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
stack = []
answer = [-1]*N
for i in range(N-1, -1, -1):
    now = lst[i]

    while stack and stack[-1] <= now:
        stack.pop()
    
    if stack:
        answer[i] = stack[-1]
    
    stack.append(lst[i])

print(*answer)
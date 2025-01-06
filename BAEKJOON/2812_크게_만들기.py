import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = input().split()[0]
stack = []

for n in num:
    while stack and stack[-1] < n and K > 0:
        stack.pop()
        K -= 1
    stack.append(n)

if K:
    print(''.join(stack[:-K]))
else:
    print(''.join(stack))
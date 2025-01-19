import sys
input = sys.stdin.readline

N = int(input())
answer = []
stack = []

now = 1
for _ in range(N):
    target = int(input())
    if answer and answer[0] == 'NO': continue

    if target >= now:
        while now <= target:
            answer.append('+')
            stack.append(now)
            now += 1
        answer.append('-')
        stack.pop()
    elif stack and target == stack[-1]:
        answer.append('-')
        stack.pop()
    else:
        answer = ['NO']

for a in answer:
    print(a)
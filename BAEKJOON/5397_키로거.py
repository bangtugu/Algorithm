import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for tc in range(T):
    temp = input().split()[0]
    left = deque()
    right = deque()
    for a in temp:
        if a == '-':
            if not left: continue
            left.pop()
        elif a == '<':
            if not left: continue
            right.appendleft(left.pop())
        elif a == '>':
            if not right: continue
            left.append(right.popleft())
        else:
            left.append(a)
    
    for a in left+right:
        print(a, end = '')
    print()
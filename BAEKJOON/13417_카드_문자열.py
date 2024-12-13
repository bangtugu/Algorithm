import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())
    lst = list(input().split())

    answer = lst[0]
    for a in lst[1:]:
        if ord(a) <= ord(answer[0]):
            answer = a + answer
        else:
            answer += a
    
    print(answer)
import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    lst = []
    already_given = set()
    for _ in range(M):
        a, b = map(int, input().split())
        lst.append([a, b])
    
    lst.sort(key = lambda x: [x[1], x[0]])
    for a, b in lst:
        for i in range(a, b+1):
            if i not in already_given:
                already_given.add(i)
                break
    
    print(len(already_given))
import sys
input = sys.stdin.readline

N = int(input())
while N:
    lst = list(map(int, input().split()))
    answer = [lst[0]]

    for i in range(1, N):
        if lst[i] > answer[-1]:
            answer.append(lst[i])
        elif lst[i] == answer[-1]: continue
        else:
            j = len(answer)-1
            while j and answer[j-1] >= lst[i]:
                j -= 1
            answer[j] = lst[i]

    print(len(answer))
    try: N = int(input())
    except: break
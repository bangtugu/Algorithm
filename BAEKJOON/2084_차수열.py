import sys
input = sys.stdin.readline

N = int(input())
degree = list(map(int, input().split()))

if sum(degree)%2:
    print(-1)
else:
    cannot = False
    answer = [[0]*N for _ in range(N)]

    sorted_left = sorted(list(range(N)), key = lambda x: -degree[x])
    
    while degree[sorted_left[0]]:
        now = sorted_left[0]

        for i in range(1, degree[now]+1):
            if i >= N or degree[sorted_left[i]] == 0:
                cannot = True
                break
            target = sorted_left[i]
            answer[now][target] = 1
            answer[target][now] = 1
            degree[target] -= 1
            degree[now] -= 1

        if cannot: break
        sorted_left = sorted(list(range(N)), key = lambda x: -degree[x])

    if cannot:
        print(-1)
    else:
        for line in answer:
            print(*line)

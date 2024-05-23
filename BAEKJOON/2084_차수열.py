import sys
input = sys.stdin.readline

N = int(input())
degree = list(map(int, input().split()))

if sum(degree)%2:
    print(-1)
else:
    answer = [[0]*N for _ in range(N)]

    ddic = {}

    for i in range(len(degree)):
        if degree[i] not in ddic.keys():
            ddic[degree[i]] = []
        ddic[degree[i]].append(i)

    k = list(ddic.keys())
    k.sort(reverse = True)

    for i in range(len(k)):
        
        for n1 in ddic[k[i]]:
            
            j = i
            while degree[n1]:
                for n2 in ddic[k[j]]:
                    if n1 == n2: continue
                    if not degree[n2]: continue

                    answer[n1][n2] = 1
                    answer[n2][n1] = 1
                    degree[n1] -= 1
                    degree[n2] -= 1
                    
                    if not degree[n1]: break
                else:
                    j += 1
                    if j >= len(k): break

    for line in answer:
        print(line)

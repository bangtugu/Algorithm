import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
if N:
    lst = sorted(list(map(int, input().split())))
    gap = sorted([lst[0]] + [lst[i] - lst[i-1] for i in range(1, N)] + [L-lst[-1]], reverse= True)
else:
    gap = [L]

answer = [[gap[i], 1] for i in range(len(gap))]
while M:
    answer[0][1] += 1
    M -= 1
    answer.sort(key = lambda x: -x[0]//x[1])

answer = answer[0][0]//answer[0][1] if not answer[0][0]%answer[0][1] else answer[0][0]//answer[0][1] + 1
print(answer)
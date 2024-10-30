import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lines = [input() for _ in range(2)]
check = [[0]*N for _ in range(2)]

lst = [[0, 0]]
check[0][0] = 1
answer = 0
for i in range(N):
    temp = []
    for line, now in lst:
        if now+K >= N:
            answer = 1
            break
        
        if not check[line][now+1] and lines[line][now+1] == '1':
            check[line][now+1] = 1
            temp.append([line, now+1])
        if now-1 > i and lines[line][now-1] == '1' and not check[line][now-1]:
            check[line][now-1] = 1
            temp.append([line, now-1])
        if lines[(line+1)%2][now+K] == '1' and not check[(line+1)%2][now+K]:
            check[(line+1)%2][now+K] = 1
            temp.append([(line+1)%2, now+K])
    
    if answer: break
    lst = temp

print(answer)
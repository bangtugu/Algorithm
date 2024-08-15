import sys
input = sys.stdin.readline

K = int(input())
N = int(input())
result = input().split()[0]

ladder = []
unknown = -1
for i in range(N):
    line = input().split()[0]
    if line[0] == '?': unknown = i
    ladder.append(line)

start = list(range(K))
end = [0]*(K)
for i in range(K):
    end[i] = ord(result[i])-65

for i in range(unknown):
    for j in range(K-1):
        if ladder[i][j] == '-':
            start[j], start[j+1] = start[j+1], start[j]

for i in range(N-1, unknown, -1):
    for j in range(K-1):
        if ladder[i][j] == '-':
            end[j], end[j+1] = end[j+1], end[j]

solved = False
answer = ''

i = 0
while i < K-1:
    if i > 0 and answer[i-1] == '-':
        answer += '*'
        i += 1
        
    elif start[i] == end[i]:
        answer += '*'
        i += 1

    elif start[i] == end[i+1] and end[i] == start[i+1]:
        answer += '-'
        i += 1
    
    else:
        break
    
else:
    solved = True

if solved:
    print(answer)
else:
    print('x'*(K-1))
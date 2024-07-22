import sys
input = sys.stdin.readline

string = input().split()[0]
target = input().split()[0]
T = len(target)

answer = []
for i in range(len(string)):
    
    answer.append(string[i])
    if string[i] == target[-1] and ''.join(answer[-T:]) == target:
        for _ in range(len(target)):
            answer.pop()

print(''.join(answer) if answer else 'FRULA')
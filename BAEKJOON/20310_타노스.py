import sys
input = sys.stdin.readline

string = input().split()[0]

N, M = 0, 0
for a in string:
    if a == '0': N += 1
    if a == '1': M += 1

N //= 2
M //= 2

answer = ''

i = 0
while i < len(string):
    if string[i] == '0' and N:
        N -= 1
        answer += '0'
    if string[i] == '1':
        if M:
            M -= 1
        else:
            answer += '1'
    
    i += 1

print(answer)
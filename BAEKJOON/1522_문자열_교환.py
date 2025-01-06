import sys
input = sys.stdin.readline

string = input().split()[0]
N = len(string)
cnt = string.count('a')

answer = N
string += string
for i in range(N):
    temp = string[i:i+cnt]
    answer = min(answer, temp.count('b'))

print(answer)
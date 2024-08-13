import sys
input = sys.stdin.readline

K = int(input())
N = int(input())
result = input().split()[0]

for _ in range(N):
    input().split()[0]

answer = [0]*(K-1)

start = list(range(K-1))
end = [0]*(K-1)
for i in range(K-1):
    end[i] = ord(end[i])-57

print(end)
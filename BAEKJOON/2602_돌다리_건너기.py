import sys
input = sys.stdin.readline

string = input().split()[0]
lst = [input().split()[0] for _ in range(2)]
N = len(string)
M = len(lst[0])
check = [[[0]*N for _ in range(M)] for _ in range(2)]

for i in range(N):
    for l in range(2):
        for j in range(M):
            if lst[l][j] != string[i]: continue
            if not i: check[l][j][i] = 1; continue
            for j2 in range(j):
                check[l][j][i] += check[1-l][j2][i-1]

answer = 0
for j in range(M):
    answer += check[0][j][N-1] + check[1][j][N-1]
print(answer)
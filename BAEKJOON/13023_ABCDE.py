import sys
input = sys.stdin.readline

N, M = map(int, input().split())
relation = [[0]*N for _ in range(N)]
friendof = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    relation[a][b] = 1
    relation[b][a] = 1
    friendof[a].append(b)
    friendof[b].append(a)


def checking(now, cnt):
    if cnt == 5:
        return True
    
    if now == -1:
        for i in range(N):
            check[i] = 1
            if checking(i, 1):
                return True
            check[i] = 0
    else:
        for i in friendof[now]:
            if check[i]: continue
            check[i] = 1
            if checking(i, cnt+1):
                return True
            check[i] = 0

    return False


check = [0]*N
answer = 1 if checking(-1, 0) else 0

print(answer)
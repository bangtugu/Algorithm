import sys
input = sys.stdin.readline

T = int(input())
dy = [-1, -1, 0, 0, 1, 1]
dx = [-1, 1, -1, 1, -1, 1]


def checking(y, x):
    for d in range(6):
        ny, nx = y+dy[d], x+dx[d]
        if 0 <= ny < N and 0 <= nx < M and not visit[ny][nx] and check[ny][nx]:
            visit[ny][nx] = 1
            if connected[ny][nx] == [-1, -1] or checking(connected[ny][nx][0], connected[ny][nx][1]):
                connected[ny][nx] = [y, x]
                return True
    
    return False


for tc in range(T):
    N, M = map(int, input().split())
    table = [input() for _ in range(N)]

    check = [[0]*M for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(M):
            if table[i][j] == '.':
                answer += 1
                check[i][j] = 1
    
    connected = [[[-1, -1] for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(0, M, 2):
            if check[i][j]:
                visit = [[0]*M for _ in range(N)]
                if checking(i, j):
                    answer -= 1

    print(answer)

'''
3
2 3
...
...
2 3
x.x
xxx
2 3
x.x
x.x
'''
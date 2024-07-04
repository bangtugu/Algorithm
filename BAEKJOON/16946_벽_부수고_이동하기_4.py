import sys
input = sys.stdin.readline

N, M = map(int, input().split())
room = []
for _ in range(N):
    line = input()
    room.append(list(line))

from collections import deque
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
group = 0
value_dic = {}
for i in range(N):
    for j in range(M):
        if room[i][j] != '0': continue

        group += 1
        room[i][j] = group
        Q = deque([[i, j]])
        cnt = 0
        while Q:
            cnt += 1
            y, x = Q.popleft()

            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if ny < 0 or ny >= N or nx < 0 or nx >= M or room[ny][nx] != '0': continue
                room[ny][nx] = group
                Q.append([ny, nx])

        value_dic[group] = cnt

answer = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if room[i][j] != '1': continue
        sett = set()
        for d in range(4):
            ny = i + dy[d]
            nx = j + dx[d]

            if ny < 0 or ny >= N or nx < 0 or nx >= M: continue
            if type(room[ny][nx]) != type(1): continue
            sett.add(room[ny][nx])

        answer[i][j] = (1+sum([value_dic[g] for g in list(sett)]))%10

for line in answer:
    print(''.join(map(str, line)))
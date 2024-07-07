import sys
input = sys.stdin.readline

N, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
entity_table = [[[] for _ in range(N)] for _ in range(N)]
entity = []
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
for i in range(K):
    y, x, d = map(int, input().split())
    y -= 1
    x -= 1
    d -= 1
    entity.append([y, x, d])
    entity_table[y][x].append(i)

answer = 0
end = False
while not end and answer < 1001:
    answer += 1
    
    for n in range(K):
        y, x = entity[n][0], entity[n][1]
        d = entity[n][2]
        
        ny = y + dy[d]
        nx = x + dx[d]
        if ny < 0 or nx < 0 or ny >= N or nx >= N or table[ny][nx] == 2: #blue
            d = d-1 if d%2 else d+1
            entity[n][2] = d
        
        ny = y + dy[d]
        nx = x + dx[d]
        if ny < 0 or nx < 0 or ny >= N or nx >= N or table[ny][nx] == 2: continue
        
        moving = []
        for i in range(len(entity_table[y][x])):
            if entity_table[y][x][i] != n: continue
            moving = entity_table[y][x][i:]
            entity_table[y][x] = entity_table[y][x][:i]
            break

        if table[ny][nx] == 1: #red
            moving = list(reversed(moving))

        entity_table[ny][nx].extend(moving)
        for t in moving:
            entity[t] = [ny, nx, entity[t][2]]

        if len(entity_table[ny][nx]) >= 4:
            end = True
            break

print(answer if answer <= 1000 else -1)
grid = [[3, 4, 6, 5, 3], [3, 5, 5, 3, 6], [5, 6, 4, 3, 6], [7, 4, 3, 5, 0]]
d = [1, -2, -1, 0, 2]
k = 2
result = 16

grid = [[3, 6, 11, 12], [4, 8, 15, 10], [2, 7, 0, 16]]
d = [1, -2, 5]
k = 3
result = 1

grid = [[0, 0, 0], [1, 0, 0], [0, 0, 0], [0, 0, 1], [1, 0, 0]]
d = [0, 0, 1, -1, 0, 0, 1, -1]
k = 10
result = 595737277


def solution(grid, d, k):
    N = len(grid)
    M = len(grid[0])
    lenth = len(d)
    
    for i in range(1, len(d)//2 + 1):
        if not len(d)%i:
            for j in range(1, len(d)//i):
                if d[:i] != d[i*j:i*(j+1)]:
                    break
            else:
                k *= len(d)//i
                d = d[:i]
            if len(d) != lenth:
                lenth = len(d)
                break

    grid2 = [[0] * (N*M) for _ in range(N*M)]
    s_grid = [0] * (N*M)
    e_grid = [0] * (N*M)
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]


    def path_finder(n, y, x, yy, xx):
        if n == lenth:
            s_grid[y*M+x] += 1
            e_grid[yy*M+xx] += 1
            grid2[y*M+x][yy*M+xx] += 1
            return

        for i in range(4):
            ny = yy + dy[i]
            nx = xx + dx[i]

            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue

            if grid[ny][nx] - grid[yy][xx] == d[n]:
                path_finder(n+1, y, x, ny, nx)

        return


    for i in range(N):
        for j in range(M):
            path_finder(0, i, j, i, j)
    

    path_dic = {
        1 : grid2
    }
    s_dic = {
        1 : s_grid
    }
    e_dic = {
        1 : e_grid
    }

    binum = ''

    while k:
        binum = str(k % 2) + binum
        k = k // 2

    for n in range(1, len(binum)):
        key = 2**n
        path_temp = path_dic[key//2]
        s_temp = s_dic[key//2]

        new_path = [[0] * (N*M) for _ in range(N*M)]
        new_e = [0] * (N*M)
        new_s = [0] * (N*M)
        
        for a in range(N*M):
            for b in range(N*M):
                if s_temp[a] and path_temp[a][b] and s_temp[b]:
                    for c in range(N*M):
                        if path_temp[b][c]:
                            new_path[a][c] += path_temp[a][b] * path_temp[b][c]
                            new_e[c] += path_temp[a][b] * path_temp[b][c]
                            new_s[a] += path_temp[a][b] * path_temp[b][c]
                        
        path_dic[key] = new_path
        e_dic[key] = new_e
        s_dic[key] = new_s

    start = False
    answer_path = [[0] * (N*M) for _ in range(N*M)]
    answer_e = [0] * (N*M)
    answer_s = [0] * (N*M)

    for n in range(len(binum)):
        if binum[-(n+1)] == '0': continue
        key = 2**n
        if not start:
            answer_path = path_dic[key]
            answer_e = e_dic[key]
            answer_s = s_dic[key]
            start = True
        else:
            now_path = path_dic[key]
            now_e = e_dic[key]
            now_s = s_dic[key]
            new_path = [[0] * (N*M) for _ in range(N*M)]
            new_e = [0] * (N*M)
            new_s = [0] * (N*M)
            
            for a in range(N*M):
                for b in range(N*M):
                    if answer_s[a] and answer_path[a][b] and now_s[b]:
                        for c in range(N*M):
                            if now_path[b][c]:
                                new_path[a][c] += answer_path[a][b] * now_path[b][c]
                                new_e[c] += answer_path[a][b] * now_path[b][c]
                                new_s[a] += answer_path[a][b] * now_path[b][c]
            
            answer_path = new_path
            answer_e = new_e
            answer_s = new_s

    return sum(answer_e) % 1000000007
    

def solutionn(grid, d, k):
    N = len(grid)
    M = len(grid[0])
    lend = len(d)
    
    s_grid = [0] * (N*M)
    e_grid = [0] * (N*M)
    grid2 = [[0] * (N*M) for _ in range(N*M)]
    temp_dic = {
        0 : [[0] * (M) for _ in range(N)],
        1 : [[0] * (M) for _ in range(N)],
        2 : [[0] * (M) for _ in range(N)],
        3 : [[0] * (M) for _ in range(N)]
    }
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    for i in range(N):
        for j in range(M):
            for z in range(4):
                if i + dy[z] < 0 or i + dy[z] >= N or j + dx[z] >= M or j + dx[z] < 0: temp_dic[z][i][j] = 5000
                else: temp_dic[z][i][j] = grid[i+dy[z]][j+dx[z]] - grid[i][j]


    def path_finder(n, y, x, yy, xx):
        if n == lend:
            grid2[y*M+x][yy*M+xx] += 1
            s_grid[y*M+x] += 1
            e_grid[yy*M+xx] += 1
            return

        for i in range(4):
            if temp_dic[i][yy][xx] == d[n]:
                path_finder(n+1, y, x, yy + dy[i], xx + dx[i])

        return


    for i in range(N):
        for j in range(M):
            path_finder(0, i, j, i, j)

    NM = N*M


    def mix_grid(fir_grid, sec_grid):
        
        new_s = [0] * NM
        new_e = [0] * NM
        new_grid = [[0] * (NM) for _ in range(NM)]

        for i in range(NM):
            if fir_grid[1][i] and sec_grid[0][i]:
                for y in range(NM):
                    if not fir_grid[2][y][i]: continue
                    for x in range(NM):
                        if not sec_grid[2][i][x]: continue
                        new_num = fir_grid[2][y][i] * sec_grid[2][i][x]
                        new_grid[y][x] += new_num
                        new_s[y] += new_num
                        new_e[x] += new_num

        return [new_s, new_e, new_grid]
    
    
    grid_dic = {
        0 : [s_grid, e_grid, grid2]
    }

    binum = ''

    while k:
        binum = str(k % 2) + binum
        k = k // 2

    for n in range(1, len(binum)):
        temp = grid_dic[n-1]
        grid_dic[n] = mix_grid(temp, temp)
        
    answer_grid = grid_dic[len(binum)-1]
    
    for n in range(1, len(binum)):
        if binum[n] == '0': continue
        
        key = len(binum)-1-n
        answer_grid = mix_grid(answer_grid, grid_dic[key])

    return sum(answer_grid[1]) % 1000000007
    

print(solutionn(grid, d, k))


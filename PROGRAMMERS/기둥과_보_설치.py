n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
result = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

# n = 5
# build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
# result = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]



def solution(n, build_frame):
    
    field = [[[False, False] for _ in range(n+1)] for _ in range(n+1)]


    def can_build(x, y, a):

        if not a:
            if y == 0 or field[y-1][x][0] or field[y][x][1] or (x-1 >= 0 and field[y][x-1][1]):
                return True    
        else:
            if y == 0:
                return False
            if field[y-1][x][0] or field[y-1][x+1][0] or (x-1 >= 0 and field[y][x-1][1] and field[y][x+1][1]):
                return True
            
        return False

    
    def can_destroy(x, y, a):
        
        if not a:
            field[y][x][a] = False
            if field[y+1][x][0] and not can_build(x, y+1, 0): field[y][x][a] = True; return False
            if field[y+1][x][1] and not can_build(x, y+1, 1): field[y][x][a] = True; return False
            if field[y+1][x-1][1] and not can_build(x-1, y+1, 1): field[y][x][a] = True; return False
        else:
            field[y][x][a] = False
            if field[y][x][0] and not can_build(x, y, 0): field[y][x][a] = True; return False
            if field[y][x+1][0] and not can_build(x+1, y, 0): field[y][x][a] = True; return False
            if field[y][x-1][1] and not can_build(x-1, y, 1): field[y][x][a] = True; return False
            if field[y][x+1][1] and not can_build(x+1, y, 1): field[y][x][a] = True; return False

        return True
    
    
    for x, y, a, b in build_frame:
        
        if 0 > x or x > n or 0 > y or y > n:
            continue
        
        if b:
            if not field[y][x][a] and can_build(x, y, a):
                field[y][x][a] = True
        else:
            if field[y][x][a] and can_destroy(x, y, a):
                field[y][x][a] = False


    answer = []
    for i in range(n+1):
        for j in range(n+1):
            if field[j][i][0]:
                answer.append([i, j, 0])
            if field[j][i][1]:
                answer.append([i, j, 1])
    return answer


print(solution(n, build_frame))
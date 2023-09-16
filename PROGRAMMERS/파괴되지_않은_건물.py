board, skill, result = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]], 10
# board, skill, result = [[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]], 6
'''
1 ≤ board의 행의 길이 (= N) ≤ 1,000
1 ≤ board의 열의 길이 (= M) ≤ 1,000
1 ≤ board의 원소 (각 건물의 내구도) ≤ 1,000
1 ≤ skill의 행의 길이 ≤ 250,000

0 ≤ r1 ≤ r2 < board의 행의 길이
0 ≤ c1 ≤ c2 < board의 열의 길이
1 ≤ degree ≤ 500
'''

def solution1(board, skill):
    
    for case in skill:
        t, y1, x1, y2, x2, d = case

        if t == 1:
            d *= -1
        
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                board[i][j] += d
    
    answer = 0
    for line in board:
        for num in line:
            if num > 0:
                answer += 1

    return answer


def solution2(board, skill):
    temp = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]

    for case in skill:
        t, y1, x1, y2, x2, d = case
        
        if t == 1:
            d *= -1

        temp[y1][x1] += d
        temp[y1][x2+1] -= d
        temp[y2+1][x1] -= d
        temp[y2+1][x2+1] += d
    
    for i in range(len(temp)):
        for j in range(1, len(temp[0])):
            temp[i][j] += temp[i][j-1]
        
    for j in range(len(temp[0])):
        for i in range(1, len(temp)):
            temp[i][j] += temp[i-1][j]

    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + temp[i][j] > 0:
                answer += 1

    return answer


print(solution2(board, skill))
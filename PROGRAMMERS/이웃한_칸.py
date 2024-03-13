'''TC1'''
board = [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]]
h = 1
w = 1
result = 2
'''TC2'''
board = [["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]]
h = 0
w = 1
result = 1


TC = 2
board = [[["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]], [["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]]]
h = [1, 0]
w = [1, 1]
result = [2, 1]


def solution(board, h, w):
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    answer = 0
    for i in range(4):
        nh = h + dy[i]
        nw = w + dx[i]
        
        if nh < 0 or nw < 0 or nw >= len(board[0]) or nh >= len(board): continue

        if board[nh][nw] == board[h][w]:
            answer += 1

    return answer


for t in range(TC):
    answer = solution(board[t], h[t], w[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, correct, comment))
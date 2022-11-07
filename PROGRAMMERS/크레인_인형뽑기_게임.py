def solution(board, moves):
    answer = 0
    pickup = []                                             # 뽑은 인형 저장하는 배열

    for move in moves:
        move -= 1                                           # 인덱스값에 맞춰 1 빼기

        for i in range(len(board)):                         # 해당 칸 위에서부터 내려오면서
            if board[i][move]:                              # 빈칸이 아니면
                pickup.append(board[i][move])               # 배열에 추가 후
                board[i][move] = 0                          # 빈칸으로 만들어주기
                break                                       # 밑으로는 탐색 X

        if len(pickup) >= 2 and pickup[-1] == pickup[-2]:   # 이후 뽑은 인형 배열 가장 위 2개가 같으면
            pickup = pickup[:-2]                            # 삭제시켜주고
            answer += 2                                     # 카운트 2 추가

    return answer
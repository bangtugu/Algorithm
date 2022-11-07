def solution(lottos, win_nums):
    lose_cnt = 0
    blank_cnt = 0
    win_cnt = 0

    for num in lottos:
        if not num:
            blank_cnt += 1
        elif num in win_nums:
            win_cnt += 1
        else:
            lose_cnt += 1

    if win_cnt == 0:
        win_cnt = 1
    if lose_cnt == 6:
        lose_cnt = 5

    return [1 + lose_cnt, 7 - win_cnt]
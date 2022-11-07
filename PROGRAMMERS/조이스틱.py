max_cnt = 0


def location(idx, lst, n):
    global max_cnt

    now_lst = lst[:]
    now_lst[idx] = 1

    if 0 not in now_lst:
        if max_cnt > n:
            max_cnt = n
        return

    if n + 1 < max_cnt:
        location(idx + 1, now_lst, n + 1)
        location(idx - 1, now_lst, n + 1)


def solution(name):
    answer = 0

    # 알파벳 위아래 변경 조작 횟수
    for i in range(len(name)):
        now = ord(name[i]) - ord('A')
        if now > 13:
            now = 13 - now % 13

        answer += now

    # 위치 변경 조작 횟수
    v = [0] * len(name)

    for i in range(len(name)):
        if name[i] == 'A':
            v[i] = 1

    global max_cnt
    max_cnt = len(name)

    location(0, v, 0)

    answer += max_cnt

    return answer
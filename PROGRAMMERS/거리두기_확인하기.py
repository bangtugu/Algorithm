from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def dfs(y, x, lst):

    v = [[-1] * 5 for _ in range(5)]

    v[y][x] = 0

    Q = deque()
    Q.append((y, x))

    while Q:
        yy, xx = Q.popleft()

        if v[yy][xx] < 2:
            for z in range(4):
                yyy = yy + dy[z]
                xxx = xx + dx[z]

                if 0 <= yyy < 5 and 0 <= xxx < 5 and v[yyy][xxx] == -1:
                    if lst[yyy][xxx] == 'P':                            # 맨해튼 거리 2 이내에 사람이 있으면 return True
                        return True
                    elif lst[yyy][xxx] == 'O':                          # 빈칸일때만 숫자 증가시켜줘서 X 배제시키면
                        v[yyy][xxx] = v[yy][xx] + 1                     # 거리 2 이내지만 X가 사이에 있는 경우를 필터링 해줌.
                        Q.append((yyy, xxx))

    return False                                                        # 맨해튼 거리 2 이내에 사람이 없으면 return False


def check(lst):

    for i in range(5):
        for j in range(5):
            if lst[i][j] == 'P':                                        # 사람이 있는 좌표에서 dfs
                cannot = dfs(i, j, lst)                                 # 거리두기가 지켜지지 않은 경우 True 반환하는 함수
                if cannot:
                    return 0                                            # 지켜지지 않았을 경우 return 0

    return 1                                                            # 중간에 return 0이 되지 않으면 return 1


def solution(places):
    answer = []

    for place in places:                                                # 5개의 원소마다 함수 실행시켜줄 반복문
        answer.append(check(place))                                     # 0, 1을 반환하는 함수로 정답 리스트에 바로 추가

    return answer

#
# places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
#
#
# print(solution(places))
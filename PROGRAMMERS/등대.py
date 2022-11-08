n = 8
lighthouse = [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]
# n = 10
# lighthouse = [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]
# n = 2
# lighthouse = [[1, 2]]


def solution(n, lighthouse):

    on_light = [0]*(n+1)                                        # 1 = 등대가 켜짐 / 2 = 등대가 켜지지 않았지만 주변 등대가 모두 빛나서 안켜도 되는 상황임
    on_light[0] = 2
    pass_lst = [[] for _ in range(n+1)]                         # 각 인덱스에 연결된 등대 번호 리스트로 저장 ( = 켜지지 않은 연결된 등대 리스트 )

    for pss in lighthouse:
        pass_lst[pss[0]].append(pss[1])
        pass_lst[pss[1]].append(pss[0])

    while 0 in on_light:                                        # 1이나 2로 판별되지 않은 등대가 있는동안 계속 반복

        for i in range(1, n+1):

            if len(pass_lst[i]) == 0 and not on_light[i]:       # 켜지지 않은 연결된 등대가 없고, 아직 on_light가 0일 때
                on_light[i] = 2                                 # 등대를 킬 필요가 없기때문에 2로 지정

            elif len(pass_lst[i]) == 1:                         # 켜지지 않은 연결된 등대가 하나만 있는 경우
                now_on = pass_lst[i][0]                         # 켜질 등대 번호 저장
                on_light[now_on] = 1                            # 해당 등대를 켜준다
                for spot in pass_lst[now_on]:                   # 연결된 등대들의 켜지지 않은 연결된 등대 리스트에서
                    pass_lst[spot].remove(now_on)               # 빼줌
                pass_lst[now_on] = []                           # 해당 등대가 켜졌으니 켜지지 않은 연결된 등대들 리스트가 필요없음

    return on_light.count(1)                                    # 켜진 등대들 갯수를 반환한다


print(solution(n, lighthouse))
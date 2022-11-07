distance = 12
scope = [[7, 8], [4, 6], [11, 10]]
times = [[2, 2], [2, 4], [3, 3]]


def solution(distance, scope, times):

    comb_lst = [[scope[i], times[i]] for i in range(len(scope))]    # 정렬하기 전에 감시범위와 근무/휴식시간 같이 묶어줌

    comb_lst.sort(key = lambda x: x[0])                             # 감시범위 기준 오름차순으로 정렬 (앞에서 걸려버리면 뒤까지 볼 필요 없기 때문)

    for watch in comb_lst:                                          # 각 경비병들에 대해서

        s = min(watch[0])                                           # 감시범위가 정렬되어있지 않으므로 (예시의 [11, 10])
        e = max(watch[0])                                           # min, max로 감시범위 시작/종료지점 특정
        w = watch[1][0]
        r = watch[1][1]

        for i in range(s, e+1):                                     # 감시지역 = 화랑이의 진행정도
            if 0 < i % (w+r) <= w:                                  # 근무+휴식시간으로 나눈 나머지값이 0이 아니고 근무시간보다 작거나 같을 때 근무시간이라 걸림
                return i                                            # 걸린 시간을 return

    return distance                                                 # 여기까지 도달했으면 모든 경비병을 통과했으므로 distance return


print(solution(distance, scope, times))
def solution(N, stages):
    total = len(stages)

    fail_cnts = [0] * (N + 2)                               # 모두 클리어한 N+1까지 고려하기 위해서 N+2까지 배열 생성

    for stage in stages:
        fail_cnts[stage] += 1                               # 각 스테이지에 머무르고 있는 사람 수 세기

    fail_pers = []

    for i in range(1, N + 1):                               # 1스테이지부터 실패율 구하기
        if total > 0:
            fail_pers.append([fail_cnts[i] / total, i])     # 실패율과 스테이지 번호 저장
        else:
            fail_pers.append([0, i])                        # 유저가 한명이라도 여기까지 오지 못했다면 실패율은 0이다.
        total -= fail_cnts[i]

    fail_pers.sort(key=lambda x: (-x[0], x[1]))             # 실패율순으로 내림차순 정렬 / 스테이지 번호순으로 오름차순 정렬

    answer = []

    for pers in fail_pers:                                  # 정답 배열에 정렬된거 스테이지 번호만 저장하기
        answer.append(pers[1])

    return answer
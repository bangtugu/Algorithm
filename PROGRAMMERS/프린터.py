from collections import deque


def solution(priorities, location):
    Q = deque()

    cnt = 0

    for i in range(len(priorities)):
        Q.append(i)                                 # deque에 인덱스값 넣어줌

    while Q:

        now = Q.popleft()

        if priorities[now] < max(priorities):       # 지금 앞에있는 인덱스값 우선순위가 젤 높지 않으면
            Q.append(now)                           # 뒤에 추가
        else:                                       # 젤 높으면
            cnt += 1                                # 카운트
            if now == location:                     # 목표 문서라면 while문 종료
                break
            priorities[now] = 0                     # 아니라면 해당 인덱스 우선순위 0으로 바꾸기

    return cnt
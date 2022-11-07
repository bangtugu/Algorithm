def solution(people, limit):
    answer = 0

    people.sort()                               # 정렬시키고

    s = 0                                       # 시작점, 끝점 정해놓고
    e = len(people) - 1

    while s <= e:
        if people[s] + people[e] > limit:       # 시작점, 끝점 같이 못태우면 끝점만 태우고 땡기기
            e -= 1
        else:                                   # 같이 태울 수 있으면 같이 땡기기
            s += 1  
            e -= 1
        answer += 1                             # 구명보트 개수는 계속 추가

    return answer
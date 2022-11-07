def solution(n, lost, reserve):
    lst = [1] * (n + 1)                                 # 학생들이 가지고있는 체육복 갯수 배열

    for s in lost:                                      # 도둑맞은애들 -1
        lst[s] -= 1
    for s in reserve:                                   # 더가져온애들 +1
        lst[s] += 1

    for i in range(n + 1):
        if lst[i] == 0:                                 # 얘가 안가져왔는데
            if i - 1 >= 0 and lst[i - 1] == 2:          # 앞에애가 2개있으면 빌려옴
                lst[i - 1] = lst[i] = 1

            elif i + 1 < n + 1 and lst[i + 1] == 2:     # 뒤에애가 2개있으면 빌려옴
                lst[i + 1] = lst[i] = 1

    return n - lst.count(0)                             # 전체인원수 - 0개인 인원 반환
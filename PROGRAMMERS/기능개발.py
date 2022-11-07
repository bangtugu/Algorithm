
def solution(progresses, speeds):
    times = []                              # 작업들이 끝날때까지 걸릴 시간

    for i in range(len(progresses)):
        progresse = progresses[i]
        speed = speeds[i]
        time = (100 - progresse) // speed
        if (100 - progresse) % speed:       # 작업들이 끝나는 시간을 구해주는 반복문
            times.append(time + 1)
        else:
            times.append(time)

    answer = []

    now = 0                                 # 현재 시간을 저장할 변수
    cnt = 0                                 # 같이 종료되는 작업들의 수를 저장하는 변수
    for i in range(len(times)):
        if times[i] > now:                  # 인덱스의 작업이 저장값보다 클 경우
            now = times[i]                  # 해당 값을 저장

            if cnt:                         # 종료되는 작업의 수가 0이 아닐때
                answer.append(cnt)          # 종료되는 작업의 수를 answer에 저장하고
                cnt = 0                     # cnt를 초기화한다.

        cnt += 1                            # 모든 작업들에서 cnt를 증가시킴.

    answer.append(cnt)                      # for문이 끝나고 남은 cnt 또한 저장해준다.

    return answer
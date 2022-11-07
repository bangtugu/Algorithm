def solution(answers):
    answer = []

    p2answer = [1, 3, 4, 5]
    p3answer = [3, 1, 2, 4, 5]

    score = [0] * 4

    for i in range(len(answers)):                               # 각 정답마다

        if answers[i] == (i % 5) + 1:                           # 1번수포자
            score[1] += 1

        if not i % 2 and answers[i] == 2:                       # 2번수포자
            score[2] += 1
        elif i % 2 and answers[i] == p2answer[(i // 2) % 4]:
            score[2] += 1

        if answers[i] == p3answer[(i // 2) % 5]:                # 3번수포자 찍은 답과 비교 후 점수 반영
            score[3] += 1

    maxscore = max(score)                                       # 점수 최대값 저장

    for i in range(4):                                          # 점수가 최대값이랑 같은사람
        if score[i] == maxscore:                                # answer 배열에 추가
            answer.append(i)

    return answer
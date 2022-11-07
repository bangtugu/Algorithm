def solution(num):
    answer = 0

    while answer != 500 and num != 1:       # 500번을 반복했거나 num이 1이 됐을때 종료되는 반복문
        answer += 1
        if num % 2:                         # 홀수면 *3 +1
            num = num * 3 + 1
        else:                               # 짝수면 /2
            num = num // 2

    if answer == 500:                       # 반복문 끝났는데 500번 반복했으면 -1로 바꿔주기
        answer = -1

    return answer
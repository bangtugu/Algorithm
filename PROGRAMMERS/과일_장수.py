def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(len(score)//m):
        answer += score[i*m + (m-1)]*m              # 내림차순으로 정렬 후 m개로 나눈 가장 마지막 값이 상자 가격
    return answer
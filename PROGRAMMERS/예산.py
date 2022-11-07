def solution(d, budget):
    if sum(d) <= budget:            # 예산이 충분하면 부서 수만큼 반환
        return len(d)

    d.sort()                        # 오름차순으로 정렬
    cnt = 0

    for i in range(len(d)):
        if budget - d[i] < 0:       # 이번 부서 돈 못주면 cnt 반환
            return cnt

        budget -= d[i]              # 예산에서 신청한 금액만큼 깎고 cnt += 1
        cnt += 1
def solution(queue1, queue2):
    
    max_cnt = len(queue1) + len(queue2)
    balance = sum(queue1) - sum(queue2)
    queue2.extend(queue1)
    queue1.extend(queue2)

    idx1 = 0
    idx2 = 0
    while balance != 0:

        if balance < 0:
            
            if idx2 >= max_cnt:
                idx1 = 0
                idx2 = -1
                break

            balance += queue2[idx2] * 2
            idx2 += 1

        else:

            if idx1 >= max_cnt:
                idx2 = 0
                idx1 = -1
                break

            balance -= queue1[idx1] * 2
            idx1 += 1
    
    answer = idx1 + idx2
    return answer
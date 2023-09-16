food_times = [1, 1, 1, 1, 5, 5, 5, 5, 5]
k = 10
result = 5

def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1 

    left = len(food_times)
    eat = 0
    min_value = 100000001
    min_cnt = 1
    while k:
        
        if k <= left:
            break

        for i in range(len(food_times)):
            if food_times[i]-eat < 0: continue

            if food_times[i] < min_value:
                min_value = food_times[i]
                min_cnt = 1
            elif food_times[i] == min_value:
                min_cnt += 1
        
        gap = min_value - eat
        
        if k >= gap * left:
            k -= gap * left
            left -= min_cnt
            eat = min_value
        else:
            cnt = k//left
            k -= cnt * left
            eat += cnt
            break

        min_value = 100000001
        min_cnt = 1


    answer = 0
    while k:
        print(k, answer, eat, food_times)
        if food_times[answer]-eat > 0:
            k -= 1
        answer += 1

    return (answer % len(food_times))+1


def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    temp = sorted(food_times)
    i = 0
    left = len(food_times)
    eat = 0
    while k:

        if k < left:
            break

        now = temp[i]
        cnt = 0
        while now == temp[i]:
            cnt += 1
            i = i + 1
            if i >= len(temp):
                break
        
        gap = now - eat
        
        if k >= gap * left:
            k -= gap * left
            left -= cnt
            eat = now
        else:
            cnt = k//left
            k -= cnt * left
            eat += cnt
            break
    
    for _ in range(k//left + 1):
        for i in range(len(food_times)):
            if food_times[i]-eat > 0:
                k -= 1
                if k == -1:
                    return i+1


print(solution(food_times, k))
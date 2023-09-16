n, info, result = 5, [2,1,1,1,0,0,0,0,0,0,0], [0,2,2,0,1,0,0,0,0,0,0]
# n, info, result = 1, [1,0,0,0,0,0,0,0,0,0,0], [-1]
# n, info, result = 9, [0,0,1,2,0,1,1,1,1,1,1], [1,1,2,0,1,2,2,0,0,0,0]
# n, info, result = 10, [0,0,0,0,0,0,0,0,3,4,3], [1,1,1,1,1,1,1,1,0,0,2]

max_gap = 0
answer = [0] * 11
def solution(n, info):
    need = [i+1 for i in info]

    def check(N, now, lst):
        if N == 0:

            now_gap = 0
            for i in range(11):
                if not info[i] and not lst[i]: continue

                if lst[i]:
                    now_gap += 10-i
                else:
                    now_gap -= 10-i

            if now_gap <= 0: return
            global max_gap
            if now_gap < max_gap: return
            global answer
            if max_gap < now_gap:
                max_gap = now_gap
                answer = [lst[i] for i in range(11)]
                return
            
            for i in range(10, -1, -1):
                if lst[i] > answer[i]:
                    answer = [lst[i] for i in range(11)]
                    return
                elif answer[i] > lst[i]:
                    return
            
            return
        
        if now == 10:
            lst[10] = N
            check(0, now, lst)
            lst[10] = 0
            return
        
        check(N, now+1, lst)
        if N >= need[now]:
            lst[now] = need[now]
            N -= need[now]
            check(N, now+1, lst)
            lst[now] = 0


    temp_lst = [0] * 11
    check(n, 0, temp_lst)

    if max_gap <= 0: return [-1]
    return answer


print(solution(n, info))
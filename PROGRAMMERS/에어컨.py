temperature = 28
t1 = 18
t2 = 26
a = 10
b = 8
onboard = [0, 0, 1, 1, 1, 1, 1]
result = 40

temperature = -10
t1 = -5
t2 = 5
a = 5
b = 1
onboard = [0, 0, 0, 0, 0, 1, 0]
result = 25

temperature = 11
t1 = 8
t2 = 10
a = 10
b = 1
onboard = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]
result = 20

temperature = 11
t1 = 8
t2 = 10
a = 10
b = 100
onboard = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]
result = 60


# def solution(temperature, t1, t2, a, b, onboard):
    
#     timeline = []
#     now = 0
#     cnt = -1
#     for i in range(len(onboard)):
#         if now == onboard[i]:
#             cnt += 1
#         elif now != onboard[i]:
#             if now:
#                 timeline.append(cnt-1)
#             else:
#                 timeline.append(cnt+1)
#             cnt = 1
#             now = onboard[i]
#     else:
#         timeline.append(cnt-1)

#     gap = abs(temperature - t2) if temperature > t2 else abs(t1 - temperature)
#     answer = a * gap
#     now = gap


#     def between(man, now, time):
#         power = 0
#         if man:
#             time -= now - gap
#             if time % 2:
#                 power = min(b*time, a*(time//2)+a, a*(time//2)+b)
#                 now = gap + 1 if power == a*(time//2)+a else gap
#             else:
#                 power = min(b*time, a*(time//2))
#                 now = gap
#         else:
#             time -= now-gap
#             now = gap
#             if time > now*2:
#                 power = min(b*time, a*gap)
#             else:
#                 if time % 2:
#                     power = min(b*time, a*(time//2)+a, a*(time//2)+b)
#                     if a*(time//2)+a == power:
#                         now = gap+1
#                 else:
#                     power = min(b*time, a*(time//2))
        
#         return power, now


#     for i in range(1, (len(timeline)//2 * 2)):
#         power, now = between(i % 2, now, timeline[i])
#         answer += power

#     return answer


def solution(temperature, t1, t2, a, b, onboard):
    
    gap = abs(temperature - t2) if temperature > t2 else abs(t1 - temperature)
    dp = [[max(a, b)*len(onboard)]*len(onboard) for _ in range(gap+2)]
    dp[0][0] = 0

    for time in range(1, len(onboard)):
        
        if onboard[time]:   s = gap
        else:               s = 0
        
        for j in range(s, gap+2):
            lst = []
            if j - 1 >= 0:      lst.append(dp[j-1][time-1] + a)
            if j:               lst.append(dp[j][time-1] + b)
            else:               lst.append(dp[j][time-1])
            if j + 1 <= gap+1:  lst.append(dp[j+1][time-1])
            dp[j][time] = min(lst)
    
    answer = min(dp[i][-1] for i in range(gap+2))
    return answer




print(solution(temperature, t1, t2, a, b, onboard))
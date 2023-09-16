play_time, adv_time, logs, result = "02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"], "01:30:59"
# play_time, adv_time, logs, result = "99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"], "01:00:00"
# play_time, adv_time, logs, result = "50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"], "00:00:00"


def solution1(play_time, adv_time, logs):
    
    
    def timetoint(string):
        h, m, s = map(int, string.split(':'))
        return h*3600 + m*60 + s
    

    def inttotime(n):
        s = str(n%60)
        m = str((n//60)%60)
        h = str(n//3600)
        if len(s) == 1: s = '0' + s
        if len(m) == 1: m = '0' + m
        if len(h) == 1: h = '0' + h
        return '{}:{}:{}'.format(h, m, s)
    

    pt = timetoint(play_time)
    at = timetoint(adv_time)

    start_lst = [pt+1]
    end_lst = [pt+1]

    for log in logs:
        start, end = log.split('-')
        start_lst.append(timetoint(start))
        end_lst.append(timetoint(end))

    start_lst.sort()
    end_lst.sort()
    lastspot = pt - at
    targets = {0, lastspot}

    for i in range(len(logs)):
        if start_lst[i] < lastspot: targets.add(start_lst[i])
        if 0 <= end_lst[i]-at < lastspot: targets.add(end_lst[i]-at)

    value_lst = [[0, 0]]
    s_idx = 0
    e_idx = 0
    now_viewer = 0
    now_time = 0
    for i in range(len(logs)*2):
        if start_lst[s_idx] <= end_lst[e_idx]:
            now_viewer += 1
            now_time = start_lst[s_idx]
            s_idx += 1
        else:
            now_viewer -= 1
            now_time = end_lst[e_idx]
            e_idx += 1
        
        if value_lst[-1][0] != now_time:
            value_lst.append([now_time, now_viewer])
        else:
            value_lst[-1][1] = now_viewer

    if now_time < pt:
        value_lst.append([pt, 0])

    adv_value = 0
    now_time = 0
    s_idx = 0
    e_idx = 0


    def get_adv_value(s):
        
        now_idx = 0
        for i in range(len(value_lst)):
            if value_lst[i][0] > s:
                now_idx = i-1
                break
        
        v = 0
        e = s + at
        while s < e:
            if value_lst[now_idx+1][0] < e:
                v += value_lst[now_idx][1] * (value_lst[now_idx+1][0] - s)
                s = value_lst[now_idx+1][0]
            else:
                v += value_lst[now_idx][1] * (e - s)
                s = e
            now_idx += 1

        return v


    adv_start_time = 0
    for target in targets:
        t_value = get_adv_value(target)
        if t_value > adv_value:
            adv_start_time = target
            adv_value = t_value
        elif t_value == adv_value:
            adv_start_time = min(adv_start_time, target)

    return inttotime(adv_start_time)


'''
대부분의 TC에서 시간초과.
log의 길이에 따라 start_lst, end_lst, value_lst, target 등 모두 크게 늘어나게 되어 시간 소모가 큰 폭으로 증가한다.

각 구간마다 몇명의 시청자가 존재할지는 알 수 있으나, target 시간에서부터의 누적 시청시간은 개별적으로 계산해야하는 비효율적인 코드.

구간합을 사용해서 각 초마다 누적 시청자 수를 구하여
광고 종료시간 누적 시청자 - 광고 시작시간 누적 시청자 = 해당 구간의 누적 시청시간 으로 누적 시청시간을 구할 수 있다.
'''


def solution2(play_time, adv_time, logs):


    def timetoint(string):
        h, m, s = map(int, string.split(':'))
        return h*3600 + m*60 + s
    

    def inttotime(n):
        s = str(n%60)
        m = str((n//60)%60)
        h = str(n//3600)
        if len(s) == 1: s = '0' + s
        if len(m) == 1: m = '0' + m
        if len(h) == 1: h = '0' + h
        return '{}:{}:{}'.format(h, m, s)
    

    pt = timetoint(play_time)
    at = timetoint(adv_time)

    viewer_lst = [0] * (pt+1)
    value_lst = [0] * (pt+1)

    for log in logs:
        start, end = log.split('-')
        viewer_lst[timetoint(start)] += 1
        viewer_lst[timetoint(end)] -= 1

    now_viewer = 0
    for i in range(len(viewer_lst)):
        if i == 0:
            value_lst[i] = viewer_lst[0]
        value_lst[i] = value_lst[i-1] + now_viewer
        now_viewer += viewer_lst[i]

    adv_start_time = 0
    max_value = 0
    lastspot = pt - at
    for start in range(lastspot+1):
        value = value_lst[start+at] - value_lst[start]
        if value > max_value:
            max_value = value
            adv_start_time = start
    
    return inttotime(adv_start_time)

print(solution2(play_time, adv_time, logs))
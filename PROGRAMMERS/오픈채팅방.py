record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]


def solution(record):
    
    user = set()
    user_name = {}
    output = []
    for line in record:
        now = line.split()

        if now[0] == 'Enter':
            if now[1] not in user:
                user.add(now[1])
            user_name[now[1]] = now[2]
            output.append([now[1], True])

        elif now[0] == 'Leave':
            output.append([now[1], False])
        
        elif now[0] == 'Change':
            user_name[now[1]] = now[2]

    answer = []
    for line in output:
        if line[1]:
            answer.append('{}님이 들어왔습니다.'.format(user_name[line[0]]))
        else:
            answer.append('{}님이 나갔습니다.'.format(user_name[line[0]]))
    
    return answer


print(solution(record))
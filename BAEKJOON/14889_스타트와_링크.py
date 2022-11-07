def calc():
    team1 = 0
    team2 = 0

    for i in range(N):
        for j in range(N):
            if team[i] and team[j]:             # 둘다 1팀일때
                team1 += status[i][j]
            elif not team[i] and not team[j]:   # 둘다 2팀일때
                team2 += status[i][j]

    return abs(team1 - team2)


def teamup(n):

    if sum(team) == N//2:

        result = calc()

        global min_val
        min_val = min(min_val, result)

        return

    if n >= N:
        return

    team[n] = 1
    teamup(n+1)
    team[n] = 0
    teamup(n+1)


N = int(input())

status = [list(map(int, input().split())) for _ in range(N)]

team = [0] * N

min_val = N//2 * 99

teamup(1)                                           # 1번째사람 0으로 고정시켜도, 나머지 경우의수에서 상대팀으로 카운트 되기때문에 시간도 반으로 줄일 수 있다.

print(min_val)
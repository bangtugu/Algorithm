N = int(input())
meetings = []
for i in range(N):
    meetings.append(tuple(map(int, input().split())))

meetings.sort(key=lambda x : (x[1], x[0]))              # 끝나는 시간 내림차순으로 정렬
                                                        # 끝나는 시간이 같은 회의들끼리는 시작하는 시간 내림차순으로 정렬
end_time = 0                                            # 이전 회의가 끝난 시간 저장
cnt = 0                                                 # 진행된 회의 숫자 저장

for meet in meetings:
    if meet[0] >= end_time:                             # 이전 회의가 끝난 시간보다 시작 시간이 늦거나 같은 경우
        end_time = meet[1]                              # 해당 회의의 끝난 시간으로 바꿔준 후
        cnt += 1                                        # 회의 숫자 +1

print(cnt)
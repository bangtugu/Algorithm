def check(lst):

    n = 0
    now = lst[0]                            # 기준 땅 설정
    now_cnt = 1                             # 기준 땅 연속횟수
    diff_h = 0                              # 다른 땅 높이 저장하는 변수
    diff_cnt = 0                            # 다른 땅 연속횟수

    while n < N-1:

        n += 1

        if lst[n] == now:                   # 기준 땅이랑 똑같으면

            if not diff_cnt:                    # 다른 땅이 감지되지 않았으면
                now_cnt += 1                    # 기준 땅 연속횟수 +1
            else:
                return 0                        # 아니면 다른 땅에 경사로가 다 설치되기 전이란 뜻. return 0
        else:
            if abs(lst[n] - now) > 1:       # 높이가 2 이상이라 경사로를 못놓으면
                return 0                    # return 0

            if not diff_cnt:                # 다른 땅이 처음 감지됐을때

                if lst[n] > now:                # 다른 땅이 기준 땅보다 높으면

                    if now_cnt < L:                 # 기준 땅 연속횟수가 경사로 길이보다 짧으면 ( 경사로 놓을수 없으면 )
                        return 0                    # return 0

                    else:                           # 기준 땅 연속횟수가 경사로 길이보다 길면 ( 경사로 놓을수 있으면 )
                        now = lst[n]                # 기준 땅 변경
                        now_cnt = 1                 # 더 높은 땅이므로 바로 경사로를 놓을 수 있음. 연속횟수 1로 초기화

                else:                           # 다른 땅이 기준 땅보다 낮으면
                    
                    diff_h = lst[n]                 # 다른 땅 변수 저장
                    diff_cnt = 1                    # 다른 땅 연속횟수 1로 초기화
                    now_cnt = 0                     # 기존 땅 연속횟수 0로 초기화

            else:                           # 다른 땅이 이미 감지된 상황에서

                if lst[n] != diff_h:            # 지금 땅의 높이가 다르면 ( 아마도 2 차이나는 높거나 낮은땅 )
                    return 0                    # return 0

                else:                           # 저장된 다른 땅과 지금 땅이 같으면
                    diff_cnt += 1               # 다른 땅 연속횟수 +1

            if diff_cnt >= L:                   # 다른 땅 연속횟수가 경사로 길이만큼 되면
                now = lst[n]                    # 기준 땅으로 교체하고
                diff_cnt = 0                    # 연속횟수도 초기화

    if diff_cnt:                        # while문이 끝났는데 diff_cnt가 남아있으면, 길 끝에 경사로를 설치하다 말았단 뜻
        return 0                        # return 0
    return 1                            # 지금까지 return되지 않았어야 경사로를 통해 통과할 수 있는 땅이므로 return 1


N, L = map(int, input().split())
NNmap = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for line in NNmap:
    ans += check(line)

for i in range(N):
    new_line = []
    for j in range(N):
        new_line.append(NNmap[j][i])
    ans += check(new_line)

print(ans)
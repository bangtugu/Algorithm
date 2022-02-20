import sys
sys.stdin = open('1940_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    speed = [list(map(int, input().split())) for _ in range(N)]
    # [[1,2],[0],[1,2],[2,1],[0],[2,4],[1,5] ~~ ]
    # 속도 저장되는 변수
    now_speed = 0
    
    # 주행거리 저장되는 변수
    distance = 0
    
    for i in range(N):
        # 1 (속도를 올려라) 일 시 now_speed에 속도 더하기
        if speed[i][0] == 1:
            now_speed += speed[i][1]

        # 2 (속도를 줄여라) 일 시 now_speed에 속도 빼기
        elif speed[i][0] == 2:
            now_speed -= speed[i][1]

            # 만약 스피드가 0 이하면 0으로
            if now_speed < 0:
                now_speed = 0

        # 결과로 나온 속도만큼 주행거리 더하기
        distance += now_speed

    print('#{} {}'.format(test_case, distance))
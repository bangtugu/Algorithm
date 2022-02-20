import sys
sys.stdin = open('2839_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    # 5kg짜리 봉지를 최대량보다 많게 설정
    # 일단 5kg짜리 봉지가 최대한 많아야 3,5kg으로 Nkg을 만들었을 때 봉지 수가 적다.
    box5 = N // 5 + 1
    box3 = 0
    N = N % 5 - 5
    cannot = False

    # 남은 N이 없을때까지 반복문 진행
    while N:
        # 5kg짜리 봉지를 하나 줄이면서
        box5 -= 1
        # 남은 kg 증가시켜줌.
        N += 5

        # 남은 설탕을 3kg짜리 봉지로 채운다.
        box3 += N // 3
        N -= 3 * (N//3)

        # 5kg짜리 봉지가 다 떨어지고 음수가 될때까지도 N이 남아있다면
        # 정확하게 N킬로그램을 만들 수 없는 것.
        if box5 < 0:
            cannot = True
    if cannot:
        total = -1
    else:
        total = box3 + box5

    print('#{} {}'.format(test_case, total))

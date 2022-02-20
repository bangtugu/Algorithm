import sys
sys.stdin = open('3462_input.txt', 'r')


# 확률 구하는 함수
def calc(per, a_per, goal):
    a_goal = 30-goal
    if goal == 30:
        return per**goal
    return (per**goal)*(a_per**a_goal)


# 경우의 수 구하는 함수
def count(n):
    cnt = 1
    for i in range(30, 30-n, -1):
        cnt *= i
    for i in range(1, n+1):
        cnt /= i
    return int(cnt)


T = int(input())

target = []
not_target = [0, 1]

# 소수 / 소수 아닌 수 나누기
for i in range(2, 31):
    for num in target:
        if i % num == 0:
            not_target.append(i)
            break
    if i not in not_target:
        target.append(i)

for test_case in range(1, T+1):
    A, B = map(int, input().split())
    a_A = (100-A)/100
    a_B = (100-B)/100
    A /= 100
    B /= 100

    # 소수가 아닐 확률 저장하는 변수
    Aper = 0
    Bper = 0

    for score in not_target:

        # 경우의 수 구하기
        cnt = count(score)

        # 확률 * 경우의 수 구하기
        AA = calc(A, a_A, score) * cnt
        BB = calc(B, a_B, score) * cnt
        Aper += AA
        Bper += BB

    # 원하는 확률 = 구한 확률이 아닐 확률 = 1 - 구한 확률
    result = 1 - Aper*Bper

    print('#{} {:.5f}'.format(test_case, result))


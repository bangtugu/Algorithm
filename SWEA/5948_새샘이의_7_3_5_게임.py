import sys
sys.stdin = open('5948_input.txt', 'r')


def check(summ, idx, n):
    if n == 3:
        # 3번 더해졌으면 리스트에 추가
        if summ not in sumlst:
            sumlst.append(summ)
        return

    if idx < 7:
        # 해당 idx에 대한 값을 추가하거나, 추가하지 않는 재귀함수 실행
        check(summ, idx+1, n)
        check(summ + numlst[idx], idx+1, n+1)


T = int(input())

for test_case in range(1, T+1):
    numlst = list(map(int, input().split()))

    sumlst = []

    check(0, 0, 0)

    # 정렬하고 5번째로 큰 수 출력
    sumlst.sort(reverse=True)
    print('#{} {}'.format(test_case, sumlst[4]))


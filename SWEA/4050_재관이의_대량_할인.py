import sys
sys.stdin = open('4050_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    # 총 가격을 구해놓고 할인받은 제품들의 가격을 빼기로 함.
    total = sum(nums)

    # 가격 내림차순 정렬
    nums.sort(reverse=True)

    # N / 3의 몫 만큼의 제품을 할인받을 수 있다.
    for i in range(N//3):
        # 할인받을 수 있는 가장 비싼 제품들은 3n 번째로 비싼 제품들이다.
        total -= nums[i*3 + 2]

    print('#{} {}'.format(test_case, total))


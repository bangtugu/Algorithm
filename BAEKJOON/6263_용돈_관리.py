# 7 5
# 100
# 400
# 300
# 100
# 500
# 101
# 400
500

N, M = map(int, input().split())

money = []

for i in range(N):
    money.append(int(input()))

minn = max(money)

maxx = sum(money)

while minn <= maxx:

    now = (minn + maxx) // 2
    left, cnt = now, 1                          # 처음 인출, 인출횟수 1

    for i in range(N):                          # 반복문을 통해 인출을 몇번 하는지 확인
        if left < money[i]:
            left = now
            cnt += 1
        left -= money[i]

    if cnt > M:             # 인출 횟수가 초과되거나, 최대 지출금액보다 인출액이 작으면 최솟값 상승
        minn = now + 1
    else:                                       # 이외의 모든 경우 최댓값 낮추기
        maxx = now - 1
        answer = now                            # 낮추면서 출력할 정답 저장

print(answer)
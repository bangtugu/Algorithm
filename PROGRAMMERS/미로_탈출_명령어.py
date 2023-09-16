n = 3
m = 4
x = 2
y = 3
r = 3
c = 1
k = 5
result = "dllrl"

# n = 2
# m = 2
# x = 1
# y = 1
# r = 2
# c = 2
# k = 2
# result = "dr"

# n = 3
# m = 3
# x = 1
# y = 2
# r = 3
# c = 3
# k = 4
# result = "impossible"


def solution(n, m, x, y, r, c, k):
    
    row = x - r if x - r > 0 else r - x
    col = y - c if y - c > 0 else c - y

    # k가 첫 출발지부터 도착지까지 충분하지 않거나, 도착지까지 거리와 k가 각각 홀수/짝수 이거나 짝수/홀수일 때 도달할 수 없음.
    if (row + col)%2 != k%2 or row + col > k:
        return "impossible"

    # 인덱스 범위 벗어나는지만 확인할 수 있으면 되기때문에 따로 리스트는 만들지 않음. 
    x -= 1
    y -= 1
    r -= 1
    c -= 1

    da = ['d', 'l', 'r', 'u']
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]

    answer = ''

    # (k - 목표지점까지 거리) 가 2 이상 남으면 어느 방향으로든 갔다가 돌아올 수 있음. (인덱스 넘어가서 못가는곳 제외) / impossible을 return했을테니 홀수로는 남지않음.
    while k - row - col >= 2:

        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m:
                x += dx[i]
                y += dy[i]
                answer = answer + da[i]
                row = x - r if x - r > 0 else r - x
                col = y - c if y - c > 0 else c - y
                k -= 1
                break
    
    # 목표지점까지 거리 = k일 때, 목표지점까지 사전순으로 탐색, 목표지점까지의 거리가 줄어드는 방향일 때 이동
    while x != r or y != c:

        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m:
                nx = x + dx[i]
                ny = y + dy[i]
                row = nx - r if nx - r > 0 else r - nx
                col = ny - c if ny - c > 0 else c - ny
                if row + col == k - 1:
                    x = nx
                    y = ny
                    answer = answer + da[i]
                    k -= 1
                    break

    return answer


print(solution(n, m, x, y, r, c, k))
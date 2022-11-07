from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def check(y, x, n):       # 영역에 포함되는 칸들을 방문처리 해주기 위한 함수

    Q = deque()
    Q.append((y, x))

    while Q:
        yy, xx = Q.popleft()
        for z in range(4):
            dyy = yy + dy[z]
            dxx = xx + dx[z]
            if 0 <= dyy < N and 0 <= dxx < N and not v[dyy][dxx]:
                v[dyy][dxx] = 1
                if area[dyy][dxx]-n > 0:
                    Q.append((dyy, dxx))


N = int(input())
area = []
maxarea = 1                                         # 아무 지역도 물에 잠기지 않을 수 있다는 내용이 있으므로 최소 1로 설정
nums = set()                                        # 모든 칸의 높이를 저장하는 세트
                                                    # (없는 높이의 경우 계산하지 않아도 되므로)
for _ in range(N):
    line = list(map(int, input().split()))
    area.append(line)
    for num in line:
        nums.add(num)

for num in nums:                                    # 존재하는 높이에 대해서

    v = [[0] * N for _ in range(N)]

    now_area = 0                                    # 현재 수위에서 존재하는 영역 갯수

    for i in range(N):
        for j in range(N):
            if area[i][j]-num > 0 and not v[i][j]:  # 수위보다 높고 방문한 적 없는 칸을 만나면
                now_area += 1                       # 영역 갯수를 1 늘리고
                v[i][j] = 1                         
                check(i, j, num)                    # 해당 영역에 포함되는 칸들을 방문한 것으로 처리하기 위해 함수 실행

    if now_area > maxarea:
        maxarea = now_area

print(maxarea)
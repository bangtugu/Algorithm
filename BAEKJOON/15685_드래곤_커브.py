dyx = [[0, 1], [-1, 0], [0, -1], [1, 0]]

'''
테이블에 드래곤커브를 배치하는 함수.
i+1세대의 드래곤 커브로 성장시킬 때,
i세대의 드래곤커브의 끝 요소부터 첫 요소까지 탐색하며 방향을 알아내고,
해당 방향을 90도 회전시켜 끝 요소에 하나하나 붙여나가면서 i+1세대의 드래곤커브를 만들어낸다.
'''


def set_dragon_curve(y, x, d, g):
    dragon_stack = [[y, x], [y+dyx[d][0], x+dyx[d][1]]]         # 주어진 좌표, 방향을 통해 0세대의 드래곤커브를 미리 생성

    for i in range(g):                                          # 세대만큼 반복하여 드래곤커브 성장시키기

        for j in range(len(dragon_stack) - 2, -1, -1):

            old_d = [dragon_stack[j][0] - dragon_stack[j+1][0], dragon_stack[j][1] - dragon_stack[j+1][1]]

            new_d = (dyx.index(old_d) + 3) % 4

            new_spot = [dragon_stack[-1][0] + dyx[new_d][0], dragon_stack[-1][1] + dyx[new_d][1]]

            dragon_stack.append(new_spot)

    for spot in dragon_stack:                   # table에 드래곤커브에 해당하는 좌표들 1로 변경시켜주기
        table[spot[0]][spot[1]] = 1


table = [[0]*101 for _ in range(101)]

N = int(input())

for _ in range(N):
    x, y, d, g = map(int, input().split())
    set_dragon_curve(y, x, d, g)                # 각각의 드래곤커브 정보에 대해서 드래곤커브 생성 함수 실행

ans = 0

for i in range(100):                            # 꼭지점 4개가 모두 드래곤커브에 해당하는 정사각형 찾기
    for j in range(100):
        if table[i][j]:
            if table[i+1][j] and table[i][j+1] and table[i+1][j+1]:
                ans += 1

print(ans)
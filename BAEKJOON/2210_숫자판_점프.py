dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

table = [list(map(int, input().split())) for _ in range(5)]

string = set()                      # 생성된 여섯자리 수 저장할 세트


def getstr(y, x, s):
    if len(s) == 6:                 # 여섯자리 수가 완성됐으면
        string.add(s)               # 세트에 add (중복 자동으로 걸러줌)
        return                      # 함수 종료

    for z in range(4):
        yy = y + dy[z]
        xx = x + dx[z]
        if 0 <= yy < 5 and 0 <= xx < 5:            # 중복된 칸을 방문해도 되므로 숫자판을 벗어났는지만 검사한다.
            getstr(yy, xx, s + str(table[yy][xx])) # 새 숫자를 포함해서 재귀함수 실행


for i in range(5):
    for j in range(5):              # 모든칸을 시작점으로 함수 실행하기
        getstr(i, j, str(table[i][j]))

print(len(string))                  # 중복되지 않은 여섯자리 수 갯수 출력
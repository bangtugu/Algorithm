import sys
sys.stdin = open('17281_input.txt', 'r')


def make_line(num):
    if num == 9:
        play(line)
        return
    if num == 3:
        line[num] = 0
        make_line(4)
    else:
        for i in range(1, 9):
            if i not in line:
                line[num] = i
                make_line(num+1)
                line[num] = 0


def play(lst):

    total = 0
    man = 0

    for i in range(N):
        field = [0, 0, 0]
        out = 0
        while out < 3:
            strike = table[i][lst[man]]
            if strike == 4:
                total += sum(field) + 1
            elif strike == 3:
                for j in range(2, -1, -1):
                    if field[j]:
                        total += 1
                        field[j] = 0
                field[2] = 1
            elif strike == 2:
                for j in range(2, 0, -1):
                    if field[j]:
                        total += 1
                        field[j] = 0
                if field[0]:
                    field[0] = 0
                    field[2] = 1
                field[1] = 1
            elif strike == 1:
                if field[2]:
                    total += 1
                    field[2] = 0
                for j in range(1, -1, -1):
                    if field[j]:
                        field[j] = 0
                        field[j+1] = 1
                field[0] = 1
            else:
                out += 1
            man = (man + 1) % 9

    global score
    score = max(score, total)


T = int(input())

for test_case in range(1, T+1):
    N = int(input())  # 진행되는 이닝 수
    table = [list(map(int, input().split())) for _ in range(N)]

    line = [0]*9

    score = 0

    make_line(0)

    print('#{} {}'.format(test_case, score))
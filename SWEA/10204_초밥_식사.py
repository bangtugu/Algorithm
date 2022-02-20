import sys
sys.stdin = open('10204_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]
    eat = [0] * n

    happy = 0

    for j in range(n):
        cnt = j % 2
        max_V = 0
        opp = 0
        for i in range(n):
            if not eat[i]:
                if table[i][cnt] > max_V:
                    max_V = table[i][cnt]
                    opp = table[i][(cnt+1)%2]
                    idx = i
                elif table[i][cnt] == max_V and table[i][(cnt+1)%2] > opp:
                    opp = table[i][(cnt+1)%2]
                    idx = i

        eat[idx] = 1

        if cnt:
            happy -= max_V
        else:
            happy += max_V


    print('#{} {}'.format(test_case, happy))
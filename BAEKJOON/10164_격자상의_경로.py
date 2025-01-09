import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())


def get_cnt(sy, sx):
    check = [[0]*sx for _ in range(sy)]
    lst = [[0, 0]]
    temp = []
    check[0][0] = 1

    while lst:
        for y, x in lst:
            for ny, nx in [[y+1, x], [y, x+1]]:
                if ny >= sy or nx >= sx: continue
                if not check[ny][nx]: temp.append([ny, nx])
                check[ny][nx] += check[y][x]
        lst = temp
        temp = []

    return check[sy-1][sx-1]


if not K:
    print(get_cnt(N, M))
else:
    my = (K-1)//M
    mx = (K-1)%M
    print(get_cnt(my+1, mx+1)*get_cnt(N-my, M-mx))
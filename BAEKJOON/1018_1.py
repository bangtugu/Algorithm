import sys
sys.stdin = open('1018_input.txt', 'r')

def mincount(row, col, sample):
    row -= 8
    col -= 8
    mincnt = 64
    for i in range(row+1):
        for j in range(col+1):
            mincnt = calcntb(i, j, sample, mincnt)
            mincnt = calcntw(i, j, sample, mincnt)
    return mincnt

def calcntb(row, col, sample, mincnt):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == j % 2:
                if sample[row+i][col+j] != 'B':
                    cnt += 1
            else:
                if sample[row+i][col+j] != 'W':
                    cnt += 1
        if cnt >= mincnt:
            return mincnt
    return cnt

def calcntw(row, col, sample, mincnt):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == j % 2:
                if sample[row + i][col + j] != 'W':
                    cnt += 1
            else:
                if sample[row + i][col + j] != 'B':
                    cnt += 1
        if cnt >= mincnt:
            return mincnt
    return cnt

T = int(input())

for test_case in range(1,T+1):
    N, M = map(int, input().split())
    table = [0] * N
    for i in range(N):
        table[i] = input()
    print (mincount(N, M, table))

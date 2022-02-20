import sys
sys.stdin = open('1018_input.txt', 'r')

def mincount():
    row = N - 8
    col = M - 8
    mincnt = 64
    for i in range(row+1):
        for j in range(col+1):
            cnt = calcnt(i, j)
            if cnt < mincnt:
                mincnt = cnt
    return mincnt

def calcnt(row, col):
    target = ['B', 'W']
    tcnt = 0
    cnt = 0
    for i in range(8):
        for j in range(8):
            if table[row+i][col+j] != target[tcnt % 2]:
                cnt += 1
            tcnt += 1
        tcnt += 1
    if cnt > 32:
        cnt = 64 - cnt
    return cnt

T = int(input())

for test_case in range(1,T+1):
    N, M = map(int, input().split())
    table = [0] * N
    for i in range(N):
        table[i] = input()
    print (mincount())

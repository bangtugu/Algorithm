import sys
sys.setrecursionlimit(15000)


def choice(n, number):

    if n == num_len:
        gap = abs(int(target)-int(number))
        global min_gap
        if gap < min_gap:
            min_gap = gap

    for i in range(10):
        if n == 0 and i == 0:
            pass
        else:
            if i not in broken:
                choice(n+1, number+str(i))


target = input()
N = int(input())
broken = list(map(int, input().split()))

simple = int(target)-100

num_len = len(str(target))

cnt = num_len
min_gap = int('9'*num_len)

choice(0, '')

cnt += min_gap

cnt += abs(int(target)-int(cnt))

print(min(cnt, simple))
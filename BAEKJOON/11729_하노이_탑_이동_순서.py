import sys
input = sys.stdin.readline

N = int(input())
cnt = 1

for _ in range(1, N):
    cnt = cnt * 2 + 1
print(cnt)


def moving(s, e, n):
    if n == 1:
        print(s, e)
    else:
        moving(s, 6-s-e, n-1)
        print(s, e)
        moving(6-s-e, e, n-1)


moving(1, 3, N)
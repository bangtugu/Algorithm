import sys
input = sys.stdin.readline
from math import comb


def poker(n):
    if n < 4:
        return 0

    cnt = n // 4
    answer = 0

    for i in range(1, cnt+1):
        answer += comb(13, i) * comb(52-4*i, n-4*i) * ((-1)**(i-1))
    
    return answer


N = int(input())
print(poker(N)%10007)
import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())

'''
GCD = 최대공약수

n을 소인수분해 한다.
1을 제외한 모든 소인수 중 하나라도 포함하는 수들 제외
나머지 수들의 갯수가 정답.

n이 최대 1조
모든 소인수들에 대해서
n - 소인수 1개 포함하는 수 + 2개 포함하는 수 - 3개 포함하는 수 ... 하면 이론상 한 수가 여러번 제외되는 일을 없앨 수 있을 것 같다.
'''

sett = set()
temp = n
while temp:
    for i in range(2, int(temp**(1/2))+1):
        if temp%i: continue
        sett.add(i)
        temp = temp//i
        break
    else:
        sett.add(temp)
        break

sett.discard(1)

lst = sorted(list(sett))
answer = n
for i in range(1, len(lst)+1):
    cnt = 0
    for now in combinations(lst, i):
        temp = 1
        for num in now:
            temp *= num
        cnt += n//temp

    answer += ((-1)**i)*cnt

print(answer)
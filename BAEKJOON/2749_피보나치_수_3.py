import sys
input = sys.stdin.readline

N = int(input())

N %= 1500000
cnt = 2
lst = [0, 1, 1]
now = 2

while cnt < N:

    cnt += 1
    now = cnt%3

    lst[now] = 0
    for i in range(3):
        if i == now: continue
        lst[now] += lst[i]%1000000

print(lst[now]%1000000)


'''

피사노 주기
피보나치 수를 M으로 나눈 나머지는 항상 주기를 가지게 된다.
M=10**k일때, k>2라면 주기는 항상 15*10**(k-1)이다.
문제에서 M = 10**6이므로, 주기는 15*10**5 = 1500000이다.

'''
import sys
input = sys.stdin.readline

N = int(input())

dic = {}
lst = list(map(int, input().split()))
sett = set(lst)
set_lst = sorted(list(sett))

for i in range(len(set_lst)):
    dic[set_lst[i]] = i

for i in range(N):
    lst[i] = dic[lst[i]]

print(*lst)
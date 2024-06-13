import sys
input = sys.stdin.readline
# sys.setrecursionlimit(1000) # 재귀시 사용

'''
1

4
140 120 160 130
1 2
1 3
1 4

2

9
120 170 170 150 160 160 140 150 150
3 1
3 7
3 8
1 9
1 4
8 2
8 5
8 6
'''

N = int(input())
iq_lst = list(map(int, input().split()))
for i in range(N-1):
    
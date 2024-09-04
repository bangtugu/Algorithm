# import sys
# input = sys.stdin.readline
# import heapq

# N, M = map(int, input().split())
# numbers = []
# HQ = []
# answer = [[0]*(N-i) for i in range(N)]

# for i in range(N):
#     now = int(input())
#     heapq.heappush(HQ, [now, i])
#     answer[0][i] = HQ[0][1]
#     answer[i][0] = i
#     numbers.append(now)

# while HQ:
#     v, idx = heapq.heappop(HQ)
#     for i in range(idx+1):
#         if answer[i][idx-i]: continue
#         for j in range(idx, N):
#             if answer[i][j-i]: break
#             answer[i][j-i] = idx

# for _ in range(M):
#     a, b = map(int, input().split())
#     if b < a:
#         a, b = b-1, a-1
#     else:
#         a -= 1
#         b -= 1
#     print(numbers[answer[a][b-a]])

'''
메모리 초과
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
lst = [0]*(N*4)


def work(s, e, n):
    if s == e:
        lst[n] = numbers[s]
        return numbers[s]
    
    m = (s + e)//2
    lv = work(s, m, n*2)
    rv = work(m+1, e, n*2+1)

    lst[n] = min(lv, rv)
    return lst[n]


def check(s, e, n):
    if a <= s and e <= b:
        return lst[n]

    if e < a or s > b: return 1000000001

    m = (s + e)//2
    lv = rv = 1000000001
    if m >= a:
        lv = check(s, m, n*2)
    if m <= b:
        rv = check(m+1, e, n*2+1)

    return min(lv, rv)


work(0, N-1, 1)
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    print(check(0, N-1, 1))
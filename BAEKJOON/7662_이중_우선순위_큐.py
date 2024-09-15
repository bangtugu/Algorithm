import sys
input = sys.stdin.readline
import heapq

T = int(input())

for tc in range(T):
    k = int(input())
    Q1 = []
    Q2 = []
    dic = {}

    cnt = 0
    for _ in range(k):
        t, num = input().split()
        num = int(num)

        if t == 'I':
            cnt += 1
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
            heapq.heappush(Q1, num)
            heapq.heappush(Q2, -num)
        
        else:
            if not cnt:
                continue
            cnt -= 1
            if num == 1:
                temp = -heapq.heappop(Q2)
                while not dic[temp]:
                    temp = -heapq.heappop(Q2)
                dic[temp] -= 1
            else:
                temp = heapq.heappop(Q1)
                while not dic[temp]:
                    temp = heapq.heappop(Q1)
                dic[temp] -= 1

    if not cnt:
        print('EMPTY')
    else:
        while not dic[Q1[0]]:
            heapq.heappop(Q1)
        while not dic[-Q2[0]]:
            heapq.heappop(Q2)
        print(-Q2[0], Q1[0])



'''
20%에서 '틀렸습니다'였다가
질문 게시판 추가 TC 확인 후 정답
'''
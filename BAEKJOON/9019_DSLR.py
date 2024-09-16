import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
str_lst = ['D', 'S', 'L', 'R']
for tc in range(T):
    start, end = map(int, input().split())

    check = set([start])
    Q = deque([[start, '']])

    answer = ''
    while Q and not answer:
        num, now = Q.popleft()
        temp = [(num*2)%10000, (num+9999)%10000, (num%1000)*10 + num//1000, (num%10) * 1000 + num//10]

        for i in range(4):
            if temp[i] in check: continue
            check.add(temp[i])
            Q.append([temp[i], now+str_lst[i]])
            if temp[i] == end:
                answer = now+str_lst[i]
                break
        
        if answer: break
    
    print(answer)


'''
pypy3로 제출시 통과, python3 시간초과
python3으로 통과한 다른사람 답안:
0~9999 모두에서 정방향, 역방향 변화값을 전부 구한다
시작값에서 정항뱡으로, 마지막값에서 역방항으로 탐색 시작, 중간값에서 만난 후 결과를 출력한다.
'''


import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
str_lst = ['S', 'L', 'R', 'D', 'D']
lst1 = [[(num+9999)%10000, (num%1000)*10 + num//1000, (num%10) * 1000 + num//10, (num*2)%10000] for num in range(10000)]
lst2 = [[(num+1)%10000, (num%10) * 1000 + num//10, (num%1000)*10 + num//1000, (10000+num)//2, num//2 if num else 5000] for num in range(10000)]

for tc in range(T):
    s, e = map(int, input().split())
    check1 = {
        s: ''
    }
    check2 = {
        e: ''
    }

    answer = ''
    Q = deque([[s, '', 1], [e, '', 0]])
    while Q and not answer:
        num, now, t = Q.popleft()

        if t:
            target_lst = lst1
            target_dic = check1
            other_dic = check2
        else:
            target_lst = lst2
            target_dic = check2
            other_dic = check1
        
        for i in range(3 if not t and num%2 else len(target_lst[num])):
            if target_lst[num][i] in target_dic: continue
            if target_lst[num][i] in other_dic:
                answer = now + str_lst[i] + other_dic[target_lst[num][i]] if t else other_dic[target_lst[num][i]] + str_lst[i] + now
                break
            else:
                target_dic[target_lst[num][i]] = target_dic[num] + str_lst[i] if t else str_lst[i] + target_dic[num]
                Q.append([target_lst[num][i], target_dic[target_lst[num][i]], t])

        if answer: break
    
    print(answer)
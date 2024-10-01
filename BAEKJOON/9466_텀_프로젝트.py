import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):

    N = int(input())
    wanted = [0] + list(map(int, input().split()))
    group = [0]*(N+1)

    answer = N
    g = 1
    for i in range(1, N+1):
        if group[i]: continue

        now = wanted[i]
        temp = set([i])
        while i != now:
            if group[now]: break
            temp.add(now)
            now = wanted[now]

            if now in temp:
                break
        
        lastnum = now
        if not group[now]:
            while not group[now]:
                group[now] = g
                answer -= 1
                now = wanted[now]
            g += 1

        if i != lastnum:
            no_group = i
            while not group[no_group]:
                group[no_group] = -1
                no_group = wanted[no_group]

    print(answer)


'''
정답 - 3564ms
'''


# import sys
# input = sys.stdin.readline

# T = int(input())

# for tc in range(T):

#     N = int(input())
#     wanted = [0] + list(map(int, input().split()))
#     group = [0]*(N+1)

#     answer = N
#     g = 0
#     for i in range(1, N+1):
#         if group[i]: continue

#         now = wanted[i]
#         temp = set([i])
#         temp_lst = [i]
#         in_group = False
#         while True:
#             if group[now]: break
#             temp.add(now)
#             temp_lst.append(now)
#             now = wanted[now]
#             if now in temp:
#                 in_group = True
#                 break
        
#         if in_group: g += 1
#         for j in range(len(temp_lst)-1, -1, -1):
#             if in_group:
#                 group[temp_lst[j]] = g
#                 answer -= 1
#                 if temp_lst[j] == now: in_group = False
#             else:
#                 group[temp_lst[j]] = -1

#     print(answer)


'''
정답 - 4004ms
오히려 시간이 늘었네?

리스트에서 역순으로 진행하면서, 사이클 내부인지 외부인지 확인하는 변수(in_group)를 통해 값을 변화시켜 방식으로 수정해봤는데,
그냥 리스트 없이 단순하게
1. (사이클이 발생했다면) 한바퀴 더 돌려보면서 그룹 지정
2. 시작점부터 다시 출발하면서 그룹없는애들 그룹없음 지정
하는게 살짝 더 빠르다.

두번째 코드가 짧고 직관적인 것 같긴 한데,
첫 코드에서는 now 변수 하나만으로 다 처리 가능한걸
두번째 코드에서는 굳이 리스트가 하나 더 추가돼서 이것저것 시간이 들어가는 것 같다.
'''
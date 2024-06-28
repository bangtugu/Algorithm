import sys
input = sys.stdin.readline

N, K = map(int, input().split())

from collections import deque

answer = 0
number_set = [set() for _ in range(K)]
Q = deque()
Q.append([str(N), 0])
cnt = 0
for n in str(N):
    if n != '0': cnt += 1

if cnt <= 1:
    print(-1)
else:
    while Q:
        num, k = Q.popleft()

        if k == K:
            answer = max(answer, int(num))
            
        else:
            numbers = [num[i] for i in range(len(num))]
            for i in range(len(numbers)):
                for j in range(i+1, len(numbers)):
                    numbers[i], numbers[j] = numbers[j], numbers[i]
                    number = ''
                    for z in range(len(numbers)):
                        number += str(numbers[z])
                    if number not in number_set[k]:
                        number_set[k].add(number)
                        Q.append([number, k+1])
                    numbers[i], numbers[j] = numbers[j], numbers[i]

    print(answer)

# numbers = []
# for n in str(N):
#     numbers.append(int(n))

# can_front = 0
# cnt = 0
# maxnum = ''
# maxnum_lst = sorted(numbers, reverse = True)
# samenum = False
# numset = set()
# for i in range(len(numbers)):
#     maxnum += str(maxnum_lst[i])
#     if numbers[i] != maxnum_lst[i]:
#         cnt += 1
#     if numbers[i]: can_front += 1
#     if numbers[i] in numset:
#         samenum = True
#     else:
#         numset.add(numbers[i])


# if can_front <= 1:
#     print(-1)
# else:
#     for _ in range(K):
#         for i in range(len(numbers)):
#             if numbers[i] == maxnum_lst[i]: continue

#             for j in range(len(numbers)-1, i, -1):
#                 if maxnum_lst[i] != numbers[j]: continue
#                 numbers[i], numbers[j] = numbers[j], numbers[i]
#                 break

#             break
#         else:
#             if samenum: break
#             numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
    
#     number = ''
#     for i in range(len(numbers)):
#         number += str(numbers[i])
#     print(int(number))



'''

16375 1

132 3

432 1

90 4

5 2

436659 2

'''
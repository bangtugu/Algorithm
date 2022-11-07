# word = input()
# N = int(input())
#
# cursor = len(word)
#
# for _ in range(N):
#     now = input()
#     if now == 'L':
#         if cursor > 0:
#             cursor -= 1
#     elif now == 'D':
#         if cursor <= len(word):
#             cursor += 1
#     elif now == 'B':
#         if cursor != 0:
#             cursor -= 1
#             word = word[:cursor]+word[cursor+1:]
#     else:
#         word = word[:cursor]+now[-1]+word[cursor:]
#         cursor += 1
#
# print(word)

'''

문자열로 하면, 최악의 경우 길이 10만의 문자열을 50만번 편집해야됨.
두개의 스택을 이용해서 가장 끝 값만 건드려주는 방식으로 속도를 올림.

'''

from sys import stdin

# 두개의 스택
word1 = list(stdin.readline().strip())
word2 = []
N = int(input())

for _ in range(N):
    now = stdin.readline().strip()
    if now[0] == 'L':
        if word1:
            word2.append(word1.pop())
    elif now[0] == 'D':
        if word2:
            word1.append(word2.pop())
    elif now[0] == 'B':
        if word1:
            word1.pop()
    elif now[0] == 'P':
        word1.append(now[-1])

# 2번째 스택은 반전시켜서 붙여줘야 한다.
print(''.join(word1 + list(reversed(word2))))
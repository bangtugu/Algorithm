import sys
input = sys.stdin.readline

line = input().split()[0]
lst = ['']
check = False
for i in range(len(line)):
    if line[i] == ':':
        lst.append('')
    else:
        lst[-1] += line[i]

answer_lst = ['' for _ in range(8)]
idx = 7
i = len(lst)-1
while i >= 0 and idx >= 0 and lst[i]:
    answer_lst[idx] = lst[i]
    i -= 1
    idx -= 1
i = 0
while i < len(lst) and lst[i]:
    answer_lst[i] = lst[i]
    i += 1

for i in range(8):
    answer_lst[i] = '0'*(4 - len(answer_lst[i])) + answer_lst[i]

answer = ''
for i in range(8):
    answer += answer_lst[i]+':' if i != 7 else answer_lst[i]

print(answer)
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(1000) # 재귀시 사용

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

group_start = list(range(N-M,N))
group_start[0] = 0
group_sum = [numbers[i] for i in group_start]
group_sum[0] = sum(numbers)-sum(group_sum[1:])

max_sum = max(group_sum)
answer = max_sum
answer_position = group_start[:]

change = True
while change:
    change = False
    for i in range(M-1):
        if group_sum[i] == max_sum:
            if group_start[i+1] > group_start[i]+1:
                change = True
                group_start[i+1] -= 1
                group_sum[i+1] += numbers[group_start[i+1]]
                group_sum[i] -= numbers[group_start[i+1]]
                break
    
    max_sum = max(group_sum)
    if answer > max_sum:
        answer = max_sum
        answer_position = group_start[:]

print(answer)
position = ''
for i in range(M-1):
    position += '{} '.format(answer_position[i+1] - answer_position[i])
position += '{}'.format(N-answer_position[-1])
print(position)
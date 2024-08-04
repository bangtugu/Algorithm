import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()

answer_v = 4000000000
answer_lst = [0, 0, 0]

for s in range(N-2):
    m, e = s+1, N-1
    s = lst[s]
    while m < e:
        value = s + lst[m] + lst[e]
        if abs(value) < answer_v:
            answer_v = abs(value)
            answer_lst = [s, lst[m], lst[e]]

        if value > 0:
            e -= 1
        elif value < 0:
            m += 1
        else:
            break
    
    if not value: break

answer = ''
for n in answer_lst:
    answer += ' ' + str(n)

print(answer)

'''

5
-2 6 -97 -6 98

7
-2 -3 -24 -6 98 100 61

'''
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
longest = [lst[0]]
check = [[0, lst[0]]]


def find(num):
    start = 0
    end = len(longest)-1

    while start <= end:
        mid = (start+end)//2

        if longest[mid] == num:
            return mid
        
        if num < longest[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return start


for i in range(1, N):
    if longest[-1] < lst[i]:
        check.append([len(longest), lst[i]])
        longest.append(lst[i])
    else:
        idx = find(lst[i])
        check.append([idx, lst[i]])
        longest[idx] = lst[i]
        
print(len(longest))
answer_lst = []
cnt = len(longest)-1
for i in range(len(check)-1, -1, -1):
    if check[i][0] == cnt:
        cnt -= 1
        answer_lst.append(check[i][1])

print(*answer_lst[::-1])
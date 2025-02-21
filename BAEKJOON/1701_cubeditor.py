import sys
input = sys.stdin.readline

string = input().split()[0]


def check(temp):
    lst = [0]*len(temp)
    j = 0
    for i in range(1, len(temp)):
        while j > 0 and temp[j] != temp[i]:
            j = lst[j-1]
        
        if temp[i] == temp[j]:
            j += 1
            lst[i] = j

    return max(lst)


answer = 0
for i in range(len(string)):
    answer = max(answer, check(string[i:]))
print(answer)
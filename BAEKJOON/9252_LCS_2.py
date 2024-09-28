import sys
input = sys.stdin.readline

str1 = '1' + input().split()[0]
str2 = '2' + input().split()[0]
lst = [[0]*len(str2) for _ in range(len(str1))]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            lst[i][j] = lst[i-1][j-1]+1
        else:
            lst[i][j] = max(lst[i][j-1], lst[i-1][j], lst[i-1][j-1])

print(lst[-1][-1])
if lst[-1][-1]:
    string = ''
    i, j = len(str1)-1, len(str2)-1
    while i and j:
        if lst[i][j]-1 == lst[i][j-1]:
            if lst[i][j]-1 == lst[i-1][j]:
                string = str2[j] + string
                i -= 1
                j -= 1
            else:
                i -= 1
        else:
            j -= 1
    
    print(string)
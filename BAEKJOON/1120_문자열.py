import sys
sys.stdin = open('1120_input.txt', 'r')

def how_many_different(string1, string2):
    if len(string1) == len(string2):
        count = 0
        for i in range(len(string1)):
            if string1[i] != string2[i]: count += 1
        return count

    if len(string1) > len(string2):
        lstr, sstr = string1, string2
    else:
        sstr, lstr = string1, string2

    mincount = len(lstr)

    for i in range(len(lstr)-len(sstr)+1):
        count = 0
        for j in range(len(sstr)):
            if lstr[i+j] != sstr[j]: count += 1
        if count < mincount: mincount = count
    return mincount


T = int(input())

for test_case in range(1, T+1):
    str1, str2 = input().split()
    different = how_many_different(str1, str2)

    print('#{} {}'.format(test_case, different))

# for test_case in range(1, T+1):
#     str1, str2 = input().split()
#     mincount = len(str2)
#     for i in range(len(str2)-len(str1)+1):
#         count = 0
#         for j in range(len(str1)):
#             if str1[j] != str2[i+j]:
#                 count += 1
#         if count < mincount:
#             mincount = count
#     print('#{} {}'.format(test_case, mincount))
import sys
input = sys.stdin.readline

N = int(input())

binum = ''

while N:
    binum = binum + str(N%2)
    N //= 2


def complex(lst1, lst2):
    new_lst = [[0, 0], [0, 0]]

    new_lst[0][0] = (lst1[0][0] * lst2[0][0] + lst1[0][1] * lst2[1][0]) % 1000000007
    new_lst[0][1] = (lst1[0][0] * lst2[0][1] + lst1[0][1] * lst2[1][1]) % 1000000007
    new_lst[1][0] = (lst1[1][0] * lst2[0][0] + lst1[1][1] * lst2[1][0]) % 1000000007
    new_lst[1][1] = (lst1[1][0] * lst2[0][1] + lst1[1][1] * lst2[1][1]) % 1000000007

    return new_lst


lst = [[[1, 2], [1, 1]] for _ in range(len(binum))]
for i in range(1, len(binum)):
    lst[i] = complex(lst[i-1], lst[i-1])

answer = 0
for i in range(len(binum)):
    if binum[i] == '1':
        if not answer:
            answer = lst[i]
            continue
        else:
            answer = complex(answer, lst[i])
    
print((answer[0][1] + answer[1][1]) % 1000000007)
import sys
input = sys.stdin.readline

dict = {'q': 0,
        'u': 1,
        'a': 2,
        'c': 3,
        'k': 4}

check = [0, 0, 0, 0, 0]


def checking(alp):

    check[dict[alp]] += 1
    if alp != 'q' and check[dict[alp]-1] < check[dict[alp]]: return True
    if alp == 'k':
        for i in range(5):
            check[i] -= 1
    return False


string = input().split()[0]
answer = 0
for a in string:
    temp = checking(a)
    if temp:
        answer = -1
        break
    else:
        answer = max(answer, max(check[:4]))
if sum(check[:4]): answer = -1

print(answer)
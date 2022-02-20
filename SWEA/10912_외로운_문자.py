import sys
sys.stdin = open('10912_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    string = input()
    lonely = []
    for alp in string:
        if not alp in lonely:
            lonely.append(alp)
        else:
            for i in range(len(lonely)):
                if lonely[i] == alp:
                    lonely.pop(i)
                    break

    if not lonely:
        result = 'Good'
    else:
        result = ''.join(list(map(chr, sorted(list(map(ord, lonely))))))

    print('#{} {}'.format(test_case,result))
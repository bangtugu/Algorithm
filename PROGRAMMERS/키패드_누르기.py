def check(left, right, num, hand):
    keypad = {
        '1': [0, 0],
        '2': [0, 1],
        '3': [0, 2],
        '4': [1, 0],
        '5': [1, 1],
        '6': [1, 2],
        '7': [2, 0],
        '8': [2, 1],
        '9': [2, 2],
        '*': [3, 0],
        '0': [3, 1],
        '#': [3, 2]
    }
    lyx = keypad[left]
    ryx = keypad[right]
    nyx = keypad[num]

    ln = abs(lyx[0] - nyx[0]) + abs(lyx[1] - nyx[1])
    rn = abs(ryx[0] - nyx[0]) + abs(ryx[1] - nyx[1])

    if (ln > rn) or (ln == rn and hand == "right"):
        right = int(num)
        ans = 'R'
    else:
        left = int(num)
        ans = 'L'

    return left, right, ans


def solution(numbers, hand):
    answer = ''
    L = '*'
    R = '#'
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            L = number
        elif number in [3, 6, 9]:
            answer += 'R'
            R = number
        else:
            L, R, ans = check(str(L), str(R), str(number), hand)
            answer += ans

    return answer
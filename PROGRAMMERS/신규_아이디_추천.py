tolower = {
    'A': 'a',
    'B': 'b',
    'C': 'c',
    'D': 'd',
    'E': 'e',
    'F': 'f',
    'G': 'g',
    'H': 'h',
    'I': 'i',
    'J': 'j',
    'K': 'k',
    'L': 'l',
    'M': 'm',
    'N': 'n',
    'O': 'o',
    'P': 'p',
    'Q': 'q',
    'R': 'r',
    'S': 's',
    'T': 't',
    'U': 'u',
    'V': 'v',
    'W': 'w',
    'X': 'x',
    'Y': 'y',
    'Z': 'z'
}

allow = list(tolower.values()) + ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '.']


def solution(new_id):

    # 대문자 소문자로
    for i in range(len(new_id)):
        if new_id[i] in tolower.keys():
            new_id = new_id.replace(new_id[i], tolower[new_id[i]])

    # 사용 안되는문자 제거하기
    for i in range(len(new_id)):
        if new_id[i] not in allow:
            new_id = new_id.replace(new_id[i], ' ')
    new_id = new_id.replace(' ', '')

    # .. -> .
    i = 0
    while i < len(new_id) - 1:
        if new_id[i:i + 2] == '..':
            new_id = new_id[:i] + '.' + new_id[i + 2:]
            i -= 1
        i += 1

    # 시작이나 끝에 있는 . 없애기
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1]

    # 빈문자열이면 a 추가
    if len(new_id) == 0:
        new_id = 'a'

    # 16자 이상이면 15자까지만으로 자르고, 잘랐는데 맨끝이 .이면 지워주기
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 3자 미만이면 3자 될때까지 마지막 문자열 붙이기
    if len(new_id) <= 2:
        while len(new_id) <= 2:
            new_id = new_id + new_id[-1]

    answer = new_id
    return answer
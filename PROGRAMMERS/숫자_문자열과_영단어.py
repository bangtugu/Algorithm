change = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def solution(s):
    for text in change.keys():
        if text in s:
            s = s.replace(text, change[text], -1)   # 문자열 숫자로 바꿔주기
    return int(s)                                   # 숫자로 변환해서 반환
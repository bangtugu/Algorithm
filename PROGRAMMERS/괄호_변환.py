def split(str):                     # 문자열을 '균형잡힌 괄호 문자열' u와 v로 분리하는 함수
    n = 0
    i = 0
    for alp in str:
        if alp == '(':
            n += 1
        else:
            n -= 1
        i += 1
        if n == 0:
            break

    return str[:i], str[i:]


def check(str):                     # 문자열이 '올바른 괄호 문자열'인지 확인하는 함수
    n = 0
    for alp in str:
        if alp == '(':
            n += 1
        else:
            n -= 1
        if n < 0:
            break

    if n < 0:
        return False
    return True


def solution(p):
    if check(p):                    # 만약 주어진 문자열이 '올바른 괄호 문자열'일 경우 해당 문자열 반환
        return p

    u, v = split(p)                 # 문자열 분리

    if check(u):                    # 3번 경우. 올바른 문자열 u는 그대로 두고, 올바르지 않은 v에 대해 모든 과정을 반복한다.
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        for alp in u[1:-1]:         # 4번 경우. 올바르지 않은 v에 대해 모든 과정을 반복하는것은 동일.
            if alp == '(':          # u는 더이상 '균형잡힌 괄호 문자열'로 분리할 수 없어 함수를 반복할 수 없는데도 '올바른 괄호 문자열'이 아니기 때문에,
                answer += ')'       # 문제에서 제시한 방법을 사용하여 가공해준다.
            else:
                answer += '('
        return answer
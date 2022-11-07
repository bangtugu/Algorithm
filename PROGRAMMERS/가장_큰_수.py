def solution(numbers):
    numbers = list(map(str, numbers))
    # numbers.sort(reverse=True)
    # numbers.sort(key = lambda x : len(x))
    numbers.sort(key = lambda x : x*3, reverse=True)
    answer = ''

    for number in numbers:
        answer += number

    if not answer or answer[0] == '0':
        return '0'
    return answer
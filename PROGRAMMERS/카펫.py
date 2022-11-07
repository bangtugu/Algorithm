def solution(brown, yellow):
    total = brown + yellow
    side = brown + 4                                            # 꼭지점 4곳이 겹치니까 4 추가해서 각 변 * 2 했을때 맞도록

    n = 1

    while total % n or 2 * n + 2 * (total // n) != side:        # n으로 나눴을때 나머지가 있거나, 가장자리 갯수가 맞지 않는동안
        n += 1

    answer = [max(n, total // n), min(n, total // n)]           # n이 더 작긴할텐데, 혹시모르니까 max/min 사용

    return answer
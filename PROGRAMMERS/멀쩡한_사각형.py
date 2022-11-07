# tc 3개 시간초과
# def solution(w, h):
#     answer = 0
# 
#     for i in range(1, w):
#         nowh = h - i * (h / w)
#         answer += int(nowh)
# 
#     answer *= 2
# 
#     return answer


# tc 6개 실패, 7개 시간초과
# def solution(w, h):
#     answer = w * h
#
#     max_num = max(w, h)
#     min_num = min(w, h)
#
#     nmin = 2
#     while w % nmin or h % nmin:
#         nmin += 1
#
#     nmax = max_num // (min_num // nmin)
#
#     ssml = 0
#
#     for i in range(1, nmax):
#         nowh = nmin - i * (nmin / nmax)
#         ssml += int(nowh)
#
#     ssml *= 2
#     smin = nmin * nmax - ssml
#
#     answer -= smin * max_num / nmax
#
#     return answer


# tc 3개 시간초과
# def solution(w, h):
#     max_num = max(w, h)
#     min_num = min(w, h)
#
#     nmin = 1
#     while (max_num * nmin) % min_num:
#         nmin += 1
#
#     slicing_num = min_num // nmin
#
#     nmax = max_num // slicing_num
#
#     ssml = 0
#
#     for i in range(1, nmax):
#         nowh = i * (nmin / nmax)
#         ssml += int(nowh)
#
#     ssml *= 2
#
#     slicing_minus = nmax * nmin - ssml
#
#     return w * h - slicing_minus * slicing_num
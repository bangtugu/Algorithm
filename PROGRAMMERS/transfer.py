import clipboard

'''
v1
'''
# lines = clipboard.paste()
# lines = lines.split('\n')

# while True:
#     for i in range(len(lines)):
#         if lines[i] == '' or lines[i] == '\r':
#             lines.remove(lines[i])
#             break
#     else:
#         break


# ex = ''
# if lines:
#     N = len(lines)
#     title = lines[0].split()
#     for i in range(1, N):
#         if lines[i]:
#             line = lines[i].split('\t')
#             for j in range(len(title)):
#                 cnt = 0
#                 ex += '{} = {}\n'.format(title[j], line[j])
#         ex += '\n'


# sample = ''
# for i in range(len(title)-1):
#     if i != 0:
#         sample += ', '
#     sample += str(title[i])
# ex += '\ndef solution({}):\n    return\n\n\nprint(solution({}))'.format(sample, sample)

# print(ex)
# clipboard.copy(ex)



'''
v2
'''
lines = clipboard.paste()
lines = lines.split('\n')

while True:
    for i in range(len(lines)):
        if lines[i] == '' or lines[i] == '\r' or lines[i] == '\n':
            lines.remove(lines[i])
            break
    else:
        break


line_dic = {}
ex = ''
if lines:
    N = len(lines)
    title = lines[0].split()
    if title[-1] == 'return':
        if 'result' not in title:
            title[-1] = 'result'
        else:
            print('예제 결과값의 변수를 지정해주세요 : ', end='')
            temp = str(input())
            title[-1] = temp
            print()
    for i in range(len(title)):
        line_dic[i] = ''
    for i in range(1, N):
        ex += '\'\'\'TC{}\'\'\'\n'.format(i)
        if lines[i]:
            line = lines[i].replace('\r', '').split('\t')
            for j in range(len(title)):
                cnt = 0
                ex += '{} = {}\n'.format(title[j], line[j])
                line_dic[j] += line[j]+', '
    ex += '\n\n'

ex += 'TC = {}\n'.format(len(lines)-1)
for i in range(len(title)):
    ex += '{} = [{}]\n'.format(title[i], line_dic[i][:-2])

sample = '{}'.format(title[0])
for i in range(1, len(title)-1):
    sample += ', {}'.format(str(title[i]))
ex += '\n\ndef solution({}):\n    \'\'\'코드 들어갈곳\'\'\'\n    return\n\n\n'.format(sample)

titles = ''
result = title[-1]+'[t]'
for i in range(len(title)-1):
    titles += title[i]+'[t], '
titles = titles[:-2]
roof_line = 'for t in range(TC):\n    answer = solution({})\n    correct = True if answer == {} else False\n    comment = "answer = {{}}".format({}) if correct else "answer = {{}} your are {{}}".format({}, answer)\n    print("TC{{}} : {{}} {{}}".format(t+1, "PASS" if correct else "FAIL", comment))'.format(titles, result, result, result)


ex += roof_line

print(ex)
clipboard.copy(ex)



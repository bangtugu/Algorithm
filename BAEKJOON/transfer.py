import clipboard

lines = clipboard.paste()
lines = lines.split('\n')

print(lines)

while True:
    for i in range(len(lines)):
        if lines[i] == '' or lines[i] == '\r' or lines[i] == '\n' or lines[i] == '힌트' or lines[i] == '출처':
            lines.remove(lines[i])
            break
    else:
        break

print(lines)

'''
예제 입력 1 
2
5 6
0 0 1 0
예제 출력 1 
30
30
예제 입력 2 
3
3 4 5
1 0 1 0
예제 출력 2 
35
17
예제 입력 3 
6
1 2 3 4 5 6
2 1 1 1
예제 출력 3 
54
-24
힌트
'''

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

# ex += 'TC = {}\n'.format(len(lines)-1)
# for i in range(len(title)):
#     ex += '{} = [{}]\n'.format(title[i], line_dic[i][:-2])

# sample = '{}'.format(title[0])
# for i in range(1, len(title)-1):
#     sample += ', {}'.format(str(title[i]))
# ex += '\n\ndef solution({}):\n    \'\'\'코드 들어갈곳\'\'\'\n    return\n\n\n'.format(sample)

# titles = ''
# result = title[-1]+'[t]'
# for i in range(len(title)-1):
#     titles += title[i]+'[t], '
# titles = titles[:-2]
# roof_line = 'for t in range(TC):\n    answer = solution({})\n    correct = True if answer == {} else False\n    comment = "answer = {{}}".format({}) if correct else "answer = {{}} your are {{}}".format({}, answer)\n    print("TC{{}} : {{}} {{}}".format(t+1, "PASS" if correct else "FAIL", comment))'.format(titles, result, result, result)


# ex += roof_line

# print(ex)
# clipboard.copy(ex)
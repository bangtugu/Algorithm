import clipboard

print('알고리즘 예제 클립보드 자동 변환기')
print('프로그래머스 = 1, 백준 = 2, SWEA = 3')
print('현재 프로그래머스만 사용 가능\n')
print('번호를 입력해주세요. : ', end = '')
problem_type = input()
print()

problem_lst = {'1', '2', '3'}
while problem_type not in problem_lst:    
    print('입력값 ({})은(는) 허용된 입력값이 아닙니다.'.format(problem_type), end = '\n')
    print('번호를 다시 입력해주세요. (프로그래머스 = 1, 백준 = 2, SWEA = 3) : ', end = '')
    problem_type = input()
    print()

problem_type = int(problem_type)



lines = clipboard.paste()
lines = lines.split('\n')
while True:
    for i in range(len(lines)):
        if lines[i] == '' or lines[i] == '\r':
            lines.remove(lines[i])
            break
    else:
        break


if problem_type == 1:
    if len(lines) < 2:
        print('문자열이 잘못되었습니다.')
        exit()
    print('프로그래머스 형식 변환')
    print()
    ex = ''
    if lines:
        N = len(lines)
        title = lines[0].split()
        for i in range(1, N):
            if lines[i]:
                line = lines[i].split('\t')
                for j in range(len(title)):
                    cnt = 0
                    ex += '{} = {}\n'.format(title[j], line[j])
            ex += '\n'
    print(ex)
    clipboard.copy(ex)
    print('예제 변수 클립보드 저장 완료. 문제풀이 파일에 붙여넣기해주세요.')

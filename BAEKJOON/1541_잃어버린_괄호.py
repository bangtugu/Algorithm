sumormin = ['-', '+']

line = input()

lst = []

nownum = ''

for i in range(len(line)):              # 숫자 / 덧셈뺄셈 기호 나눠서 리스트에 넣어주는 반복문
    if line[i] in sumormin:
        lst.append(int(nownum))
        lst.append(line[i])
        nownum = ''
    else:
        nownum += line[i]

lst.append(int(nownum))                 # 마지막 숫자까지 리스트에 넣어줌.

result = 0                              # 결과값 저장하는 변수
plus = True                             # -를 만났는지 확인하는 변수

for i in range(len(lst)):
    if not i%2:
        if plus:
            result += lst[i]
        else:
            result -= lst[i]
    elif plus and lst[i] == '-':
        plus = False

print(result)

'''
    가장 최소값을 출력해야 한다.
    괄호를 적절히 씌운다면 주어진 식의 첫번째 - 이후의 모든 값들을 그 이전 값에 대해서 뺄셈으로 적용할 수 있기 때문에,
    첫번째 - 만 감지하여 그 전의 값들은 더하고 그 후의 값들은 전부 빼준다.
'''
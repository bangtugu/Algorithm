N = int(input())

numb = {}                                           # 알파벳 자릿수 기록할 dict

for _ in range(N):                                  # 알파벳 자릿수 저장하는 반복문
    word = input()
    for i in range(len(word)):
        if word[i] not in numb.keys():              # dict에 해당 알파벳 없으면 생성
            numb[word[i]] = 0
        numb[word[i]] += 10 ** (len(word) - (i+1))  # 자릿수 저장

numbers = []

for number in numb.values():                        # 저장된 자릿수들을 모두 배열에 옮긴다.
    if number:
        numbers.append(number)

numbers.sort(reverse=True)                          # 내림차순으로 정렬

result = 0
temp = 9
for number in numbers:                              # 가장 큰 값의 알파벳에 9를 배정하고
    result += number * temp                         # 곱해서 결과에 저장
    temp -= 1                                       # 배정할 수를 1씩 줄인다.

print(result)
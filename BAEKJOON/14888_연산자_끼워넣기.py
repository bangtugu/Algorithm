def calc(txt):

    txt = list(txt.split())                 # 완성된 계산식 배열로 변환

    ans = int(txt[0])                       # */ -> +-의 기존 연산 순서는 무시하므로 가장 첫 수를 변수에 저장

    n = 1
    while n < len(txt):                     # 이후 나오는 연산자에 따라 연산자 바로 뒷 수에 대해서 계산 진행.
        if txt[n] == '+':                   # 계산식은 항상 숫자로 끝나므로 연산자 인덱스 +1 했을때 인덱스 에러 날 경우는 없음.
            ans += int(txt[n+1])

        elif txt[n] == '-':
            ans -= int(txt[n+1])

        elif txt[n] == '*':
            ans *= int(txt[n+1])

        else:
            if ans < 0:
                ans = ((ans * (-1)) // int(txt[n+1])) * (-1)        # 나눗셈 할때만 혹시모르니까 양수/음수 따로 처리했음.
            else:
                ans = ans // int(txt[n+1])

        n += 2

    global max_num
    max_num = max(max_num, ans)

    global min_num
    min_num = min(min_num, ans)


def making(n, t, txt):

    txt = txt + ' ' + numbers[n] + ' ' + tools[t]   # 계산식 문자열로 생성

    if n >= N-2:                                    # ex) 숫자가 2개면 0번 인덱스면 연산자가 모두 사용되므로 N-1
        calc(txt + ' ' + numbers[-1])               # 다음 함수 실행
        return

    for i in range(4):
        if tools_dic[tools[i]]:
            tools_dic[tools[i]] -= 1
            making(n+1, i, txt)
            tools_dic[tools[i]] += 1


tools = ['+', '-', '*', '/']
tools_dic = {
    '+': 0,
    '-': 0,
    '*': 0,
    '/': 0
}

N = int(input())
numbers = list(input().split())
tools_cnt = list(map(int, input().split()))

for i in range(4):
    tools_dic[tools[i]] = tools_cnt[i]

min_num = 1000000000                            # 문제에서 주어진 최대/최솟값 뒤집어서 초기화
max_num = -1000000000

for i in range(4):
    if tools_dic[tools[i]]:                     # dict에 해당 연산자 남아있을때만
        tools_dic[tools[i]] -= 1                # 
        making(0, i, '')                        # 다른 경우의 수에서 활용 가능하게 함수 끝나면 값 복구시키기
        tools_dic[tools[i]] += 1                # 

print(max_num)
print(min_num)
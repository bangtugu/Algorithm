import sys
input = sys.stdin.readline

N = input().split()[0]
answer = [0]*10

for i in range(len(N)):
    limit = int(N[i])

    for j in range(10):
        if i == j == 0: continue # 첫째자리에는 0이 올수 없다.
        if i == 0 and j > limit: break # 첫째자리의 경우 주어진 값을 넘어가면 세지 않는다.
        
        num1, num2 = 1, 1
        
        if i: num1 = int(N[:i]) # 첫째자리가 아닌경우 왼쪽값의 변수 변경
        
        num2 = 10**(len(N)-i-1) if i <= len(N)-1 else 1 # 오른쪽값 변수 (자릿수에만 영향 받음)

        if j == limit:
            answer[j] += int(N[i+1:])+1 if N[i+1:] else 1 # 주어진 값일 경우 오른쪽 나머지값만큼 추가
            if not i or not j: # 첫째자리이면 num1을 0으로 만들기 위해, 현재 고려하는중인 j가 0인 경우 0이 맨 앞자리인 1가지의 경우를 제외함
                num1 -= 1
        if i and j and j < limit: # 첫째자리가 아니면서 주어진 값보다 작을 경우, 해당 숫자를 넘어 진행될 것이기 때문에 1 추가
            num1 += 1

        answer[j] += num1*num2
    
print(*answer)


'''
12345

1xxxx = 2346개 (answer[1] += 2346)
x1xxx = 2(0~1)*1000 = (answer[1] += 10000)
xx1xx = 13(0~12)*100 = (answer[1] += 1300)
xxx1x = 124(0~123)*10 = (answer[1] += 1240)
xxxx1 = 1235(0~1234)*1 = (answer[1] += 1235)

'''
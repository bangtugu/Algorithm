N, r, c = map(int, input().split())

answer = 0

while N > 0:

    N -= 1
    temp = 2**(N*2)
    if 2**N <= r:
        answer += temp*2
        r -= 2**N
    if 2**N <= c:
        answer += temp
        c -= 2**N

print(answer)

'''
예제 입력 1 
2 3 1
예제 출력 1 
11
예제 입력 2 
3 7 7
예제 출력 2 
63
예제 입력 3 
1 0 0
예제 출력 3 
0
'''
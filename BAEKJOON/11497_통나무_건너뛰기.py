T = int(input())

for test_case in range(T):
    N = int(input())
    result = [0]*N
    wood = list(map(int, input().split()))
    wood.sort()                                 # 정렬해서 높이 받기

    for i in range(N):
        if i%2:
            result[i//2] = wood[i]              # 앞/뒤로 번갈아서 넣기
        else:
            result[-(i//2)-1] = wood[i]

    max_num = 0
    for i in range(N):
        if i != N-1:
            now = abs(result[i]-result[i+1])    # 가장 큰 높이 차이 구하기
        else:
            now = abs(result[i]-result[0])
        if now > max_num:
            max_num = now

    print(max_num)
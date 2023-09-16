n, k, result = 437674, 3, 3
# n, k, result = 110011, 10, 2


def solution(n, k):
    num = ''
    while n >= k:
        num = str(n%k) + num
        n //= k
    num = str(n) + num

    lst = []
    for string in list(num.split('0')):
        if string and string != '1':
            lst.append(int(string))


    def is_prime_num(N):
        for j in range(3, int(N**(1/2))+1, 2):      # 제곱근까지만 판별하면 됨 N까지 판별하라하면 1번 tc에서 시간초과
            if N%j == 0:
                return False
        
        return True


    prime_num = set()
    prime_num.add(2)
    
    answer = 0
    for num in lst:
        if num in prime_num:
            answer += 1
        elif is_prime_num(num):
            prime_num.add(num)
            answer += 1
    
    return answer


print(solution(n, k))
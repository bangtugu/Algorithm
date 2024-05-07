'''TC1'''
n = 3
count = 1
result = 8
'''TC2'''
n = 3
count = 2
result = 6
'''TC3'''
n = 3
count = 3
result = 1


TC = 5
n = [3, 3, 3, 4, 4]
count = [1, 2, 3, 1, 3]
result = [8, 6, 1, 48, 12]


def solution(n, count):


    def get_cnt(middle):
        cnt = 0
        for numbers in middle:
            if not numbers: continue
            N = len(numbers)

            temp = N
            for i in range(N-1, 1, -1):
                temp *= i

            # N >= 3일때 점화식 ???
            
            cnt += temp

        return cnt if cnt else 1


    def get_middle(n, front, lst):
        cnt = 0
        if n == 0:
            cnt += get_cnt(lst)
        elif n in front:
            cnt += get_middle(n-1, front, lst)
        else:
            for i in range(len(lst)):
                if front[i//2] < n: continue
                lst[i].append(n)
                cnt += get_middle(n-1, front, lst)
                lst[i].pop()

        return cnt % 1000000007
    

    def get_front(n, count, lst):

        cnt = 0
        if len(lst) == count:
            lst.sort()
            cnt += get_middle(n, lst, [[] for _ in range(count*2)])
        else:
            for i in range(lst[-1]-1, 0, -1):
                cnt += get_front(n, count, lst+[i])

        return cnt % 1000000007


    answer = get_front(n, count, [n])

    return answer % 1000000007


def solution(n, count):

    table = [[0]*(n+1) for _ in range(n+1)]

    table[1][1] = 1
    
    for i in range(1, n):
        for j in range(1, n):
            table[i+1][j+1] += table[i][j]
            table[i+1][j] += table[i][j]*i*2

    '''
    n,cnt -> n+1,cnt == 맨 앞을 제외한 모든 자리에 11을 꽂아넣는것과 같다. == n,cnt의 모든 경우(n,cnt)에 대해 n*2만큼 꽂아넣는 경우가 있음. == n+1,cnt = n,cnt*n*2
    n,cnt -> n+1,cnt+1 == 11을 맨 앞에 꽂아넣는것과 같다. == n,cnt의 모든 경우(n,cnt)만큼 꽂아넣는 경우가 있음. == n+1,cnt+1가 n,cnt를 포함 (위의 조건에 의해 n,cnt+1*n*2 또한 포함) 
    n+1,cnt+1 = n,cnt + n,cnt+1*n*2
    '''

    return table[n][count] % 1000000007


for t in range(TC):
    answer = solution(n[t], count[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))
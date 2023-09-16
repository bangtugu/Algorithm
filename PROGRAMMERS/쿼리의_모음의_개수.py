ex = [
    2,	[1,2],	4,
    3,	[3],	19,
    5,	[1,4,4],	157740,
    50,	[1,6,5,2,4],	61953538
    ]


def solution(q, a):

    N = len(a)
    M = max(a)

    pos_dic = {}
    for i in range(1, M+1):
        pos_dic[i] = []
    

    for i in range(M, 0, -1):
        for j in range(N):
            if a[j] >= i:
                pos_dic[i].append(j)

    print(pos_dic)
    pos_lst = []


    # 필수 쿼리 리스트 만들기
    # 필수 쿼리 조합 만들기
    # 필수 쿼리 조합마다, 가능한 쿼리 조합 갯수 찾고 갯수 반환
    


    answer = -1
    return answer


for i in range(4):
    q = ex[i*3]
    a = ex[i*3+1]
    result = ex[i*3+2]
    print(q, a, result)
    if solution(q, a)%998244353 == result:
        print('Pass')
    else:
        print('Fail')
import sys
sys.stdin = open('3584_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    # 노드 수
    N = int(input())

    table = [0] * (N+1)

    # 간선 정보 (N-1개)
    for _ in range(N-1):
        p, c = map(int, input().split())
        table[c] = p

    t1, t2 = map(int, input().split())

    p_lst = []

    # t1에서 루트까지 정점 리스트 생성
    while t1:
        p_lst.append(t1)
        t1 = table[t1]

    # t1~루트 리스트에 있는 값일때까지 t2에서 루트로 이동
    while t2 not in p_lst:
        t2 = table[t2]

    print(t2)


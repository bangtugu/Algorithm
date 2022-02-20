import sys
sys.stdin = open('2382_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())

    samples = [list(map(int, input().split())) for _ in range(K)]

    print(N, M, K)
    print(samples)
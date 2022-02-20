import sys
sys.stdin = open('1808_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    table = list(map(int, input().split()))
    N = int(input())

    complete = False

    while not complete:
        
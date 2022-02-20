import sys
sys.stdin = open('5658_input.txt', 'r')

table = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    sample = input()

    alps = []
    numbers = []

    for i in range(N//4):
        if i:
            now_sample = sample[-i:] + sample[:N-i]
        else:
            now_sample = sample
        for j in range(4):
            now = now_sample[N//4 * j:N//4 * (j+1)]
            if now not in alps:
                alps.append(now)
                num = 0
                for z in range(len(now)):
                    num += table[now[z]] * 16**(len(now)-z-1)
                numbers.append(num)

    numbers.sort(reverse=True)

    print('#{} {}'.format(test_case, numbers[K-1]))
import sys
sys.stdin = open('6603_input.txt', 'r')


def lotto(n, lst):
    if len(lst) == 6:
        print(*lst)
        return

    for i in range(n, len(T)):
        if not v[i]:
            v[i] = 1
            lotto(i, lst + [T[i]])
            v[i] = 0

T = [1]

while T != [0]:
    T = list(map(int, input().split()))
    v = [0] * len(T)
    lotto(1, [])
    print()


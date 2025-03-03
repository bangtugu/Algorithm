import sys
input = sys.stdin.readline


def check(n):
    temp = [0]*10

    for i in range(len(n)):
        now = int(n[i])

        for j in range(10):
            if i == j == 0: continue
            if i == 0 and j > now: break

            left, right = 1, 1

            if i: left = int(n[:i])

            right = 10**(len(n)-i-1) if i <= len(n)-1 else 1

            if j == now:
                temp[j] += int(n[i+1:])+1 if n[i+1:] else 1
                if not i or not j:
                    left -= 1
            if i and j and j < now:
                left += 1

            temp[j] += left*right

    return sum(list([i*temp[i] for i in range(1, 10)]))


L, U = input().split()
U = check(U)
L = check(str(int(L)-1)) if int(L) else 0
print(U-L)
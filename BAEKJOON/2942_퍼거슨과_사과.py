import sys
input = sys.stdin.readline

R, G = map(int, input().split())


def get_lst(n):
    sett = set()

    for i in range(1, int(n**(1/2))+1):
        if not n%i:
            sett.add(i)
            sett.add(n//i)

    return sorted(list(sett))


lst = get_lst(min(R, G))
for i in lst:
    if not R%i and not G%i:
        print(i, R//i, G//i)
import sys
input = sys.stdin.readline

A, B = map(int, input().split())


def is_complex(n1, n2):

    start = int(n1**(1/2))
    while start > 1:
        if not n1%start and not n2%start:
            return True
        start -= 1

    return False


BA = B//A
C = int(BA**(1/2))
D = 0
while not D:
    while BA % C:
        C -= 1
    
    if is_complex(C, BA//C):
        C -= 1
    else:
        D = BA//C

print(A*C, A*D)
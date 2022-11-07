# A1, A2 = map(int, input().split())
# B1, B2 = map(int, input().split())
#
# C1, C2 = A1*B2 + B1*A2, A2*B2
#
# D = 1
#
# for i in range(min(C1, C2)+1, -1, -1):
#     if not ( C1 % i or C2 % i ):
#         D = i
#         break
#
# print(C1//D, C2//D)
# 시간초과


# 최대공약수 구하는 함수
def calc(n1, n2):
    while n1 % n2 != 0:
        temp = n1 % n2
        n1 = n2
        n2 = temp
    return n2


A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

C1 = calc(A2, B2)

D1, D2 = A1*B2//C1 + B1*A2//C1, A2*B2//C1

C2 = calc(D1, D2)

print(D1//C2, D2//C2)
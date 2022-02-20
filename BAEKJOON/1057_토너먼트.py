
def nex(num):
    return num//2 + num%2

N, p1, p2 = map(int, input().split())
p1, p2 = min(p1, p2), max(p1, p2)
Round = 1

while not p1%2 or p2 != p1 + 1:
    p1, p2 = nex(p1), nex(p2)
    Round += 1

print(Round)
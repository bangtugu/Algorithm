import sys
input = sys.stdin.readline

S, E, Q = input().split()


def get_time(string):
    time = 0
    time += int(string[:2])*60
    time += int(string[3:5])
    return time


S, E, Q = get_time(S), get_time(E), get_time(Q)
sett, sset, eset = set(), set(), set()
while True:
    try:
        time, name = input().split()
    except:
        break
    T = get_time(time)
    sett.add(name)
    
    if T <= S:
        sset.add(name)
    elif E <= T <= Q:
        eset.add(name)

answer = 0
for member in list(sset):
    if member in sset and member in eset:
        answer += 1

print(answer)
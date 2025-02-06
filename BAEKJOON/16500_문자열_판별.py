string = input()
N = int(input())
strdic = {}
cnt = {}
for _ in range(N):
    s = input()
    if s[0] not in strdic: strdic[s[0]] = []
    if s not in cnt: cnt[s] = 0
    strdic[s[0]].append(s)
    cnt[s] += 1
check = set()


def checking(i):
    if i == len(string): return True
    if string[i] not in strdic: return False
    for s in strdic[string[i]]:
        if not cnt[s]: continue
        if string[i:i+len(s)] == s:
            cnt[s] -= 1
            if checking(i+len(s)): return True
            cnt[s] += 1


print(1 if checking(0) else 0)
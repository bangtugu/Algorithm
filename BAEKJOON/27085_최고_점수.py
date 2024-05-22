import sys
input = sys.stdin.readline


N, S = map(int, input().split())
room = list(map(int, input().split()))
passvalue = room[:]
S -= 1

for i in range(1, S):
    if passvalue[i-1] > 0:
        passvalue[i] += passvalue[i-1]
    
for i in range(N-2, S, -1):
    if passvalue[i+1] > 0:
        passvalue[i] += passvalue[i+1]

l, r = S-1, S+1
answer = 0
while True:
    if l >= 0 and room[l] >= 0:
        answer += room[l]
        l -= 1
        continue
    if r < N and room[r] >= 0:
        answer += room[r]
        r += 1
        continue
    break

while True:
    
    if l >= 0 and passvalue[l] >= 0:
        now = answer
        temp = answer
        tl = l
        while l >= 0 and passvalue[l] >= 0 and now + room[l] >= 0:
            now += room[l]
            l -= 1
            if now >= answer:
                answer = now
                tl = l
        l = tl
        if answer != temp: continue

    if r < N and passvalue[r] >= 0:
        now = answer
        temp = answer
        tr = r
        while r < N and passvalue[r] >= 0 and now + room[r] >= 0:
            now += room[r]
            r += 1
            if now >= answer:
                answer = now
                tr = r
        r = tr
        if answer != temp: continue
        
    break

print(answer)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()
cover = 0
answer = 0
for s, e in lst:
    if s <= cover:
        s = cover + 1
    
    if s >= e: continue

    cnt = (e-s)//K
    cnt += 1 if (e-s)%K else 0

    answer += cnt
    cover = s+cnt*K-1

print(answer)
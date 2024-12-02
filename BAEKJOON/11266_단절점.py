import sys
input = sys.stdin.readline
sys.setrecursionlimit(11000)

V, E = map(int, input().split())
connected = [[] for _ in range(V+1)]

for _ in range(E):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)

check = [0]*(V+1)
answer = []


def dfs(now, last, cnt):
    check[now] = cnt
    going, split = 0, 0
    min_connected = V
    for n in connected[now]:
        if n == last: continue
        if not check[n]:
            going += 1
            next_min_connected = dfs(n, now, cnt+1)
            if next_min_connected >= cnt:
                split = 1
            min_connected = min(next_min_connected, min_connected)
        else:
            min_connected = min(min_connected, check[n])

    if cnt == 1 and going >= 2 or cnt != 1 and split:
        answer.append(now)
    
    return min_connected
    

for i in range(1, V+1):
    if not check[i]:
        dfs(i, i, 1)

print(len(answer))
if answer: print(*sorted(answer))